from ExprVisitor import ExprVisitor
from ExprParser import ExprParser
import sys

class EvalVisitor(ExprVisitor):
    def __init__(self):
        self.memory = {}   
        self.types = {}    
        self.declared = set()  
        self.type_errors = []
        
    def visitProg(self, ctx):
        print("visitProg called")
        results = []
        for cmd in ctx.command():
            result = self.visit(cmd)
            if result is not None:
                results.append(result)
        return results
        
    def visitCommand(self, ctx):
        return self.visit(ctx.statement())
    
    def visitEmptyStatement(self, ctx):
        return None
        
    def visitAssignment(self, ctx):
        id_name = ctx.ID().getText()
        
        if id_name not in self.declared:
            self.type_errors.append(f"Variable '{id_name}' used before declaration")
            return None
            
        value = self.visit(ctx.expr())
        
        expected_type = self.types[id_name]
        
        if expected_type == 'float' and isinstance(value, int):
            value = float(value)  
        
        if not self._check_type_compatibility(value, expected_type):
            self.type_errors.append(f"Type error: Cannot assign {type(value).__name__} to variable '{id_name}' of type {expected_type}")
            return None
            
        self.memory[id_name] = value
        
        return value 
        
    def visitDeclaration(self, ctx):
        type_name = self.visit(ctx.type_())
        
        for id_node in ctx.ID():
            id_name = id_node.getText()
            
            if id_name in self.declared:
                self.type_errors.append(f"Variable '{id_name}' already declared")
                continue
                
            self.declared.add(id_name)
            self.types[id_name] = type_name
            
            if type_name == 'int':
                self.memory[id_name] = 0
            elif type_name == 'float':
                self.memory[id_name] = 0.0
            elif type_name == 'bool':
                self.memory[id_name] = False
            elif type_name == 'string':
                self.memory[id_name] = ""
            if type_name == 'FILE':
                self.memory[id_name] = None 
                
        return None
        
    def visitDeclarationWithAssignment(self, ctx):
        type_name = self.visit(ctx.type_())
        id_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        if type_name == 'FILE':
            if not isinstance(value, str):
                self.type_errors.append(f"Type error: Cannot assign {type(value).__name__} to variable '{id_name}' of type FILE")
                return None
            self.memory[id_name] = value
            self.types[id_name] = 'FILE'
            self.declared.add(id_name)
            return value
        
        if id_name in self.declared:
            self.type_errors.append(f"Variable '{id_name}' already declared")
            return None
            
        self.declared.add(id_name)
        self.types[id_name] = type_name
        
        value = self.visit(ctx.expr())
        
        if not self._check_type_compatibility(value, type_name):
            self.type_errors.append(f"Type error: Cannot assign {type(value).__name__} to variable '{id_name}' of type {type_name}")

            if type_name == 'int':
                self.memory[id_name] = 0
            elif type_name == 'float':
                self.memory[id_name] = 0.0
            elif type_name == 'bool':
                self.memory[id_name] = False
            elif type_name == 'string':
                self.memory[id_name] = ""
            if type_name == 'FILE':
                self.memory[id_name] = None
        else:
            self.memory[id_name] = value
            
        return None
    
    def visitReadStatement(self, ctx):
        for id_node in ctx.ID():
            id_name = id_node.getText()
            
            if id_name not in self.declared:
                self.type_errors.append(f"Variable '{id_name}' used before declaration")
                continue
                
            var_type = self.types[id_name]
            
            try:
                input_value = input(f"Enter value for {id_name} ({var_type}): ")
                
                if var_type == 'int':
                    value = int(input_value)
                elif var_type == 'float':
                    value = float(input_value)
                elif var_type == 'bool':
                    if input_value.lower() in ('true', 't', '1', 'yes', 'y'):
                        value = True
                    elif input_value.lower() in ('false', 'f', '0', 'no', 'n'):
                        value = False
                    else:
                        self.type_errors.append(f"Invalid boolean value for variable '{id_name}': {input_value}")
                        continue
                elif var_type == 'string':
                    value = input_value
                else:
                    self.type_errors.append(f"Unknown type for variable '{id_name}': {var_type}")
                    continue
                    
                self.memory[id_name] = value
                    
            except ValueError:
                self.type_errors.append(f"Invalid input for variable '{id_name}' of type {var_type}")
                
        return None
        
    def visitWriteStatement(self, ctx):
        values = []
        for expr_ctx in ctx.expr():
            value = self.visit(expr_ctx)
            values.append(value)
            
        print(" ".join(str(val) for val in values))
        
        return None
        
    def visitBlockStatement(self, ctx):
        for stmt_ctx in ctx.statement():
            self.visit(stmt_ctx)
            
        return None
        
    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.expr())
        
        if not isinstance(condition, bool):
            self.type_errors.append(f"Type error: If condition must be boolean, got {type(condition).__name__}")
            return None
            
        if condition:
            self.visit(ctx.statement())
            
        return None
        
    def visitIfElseStatement(self, ctx):
        condition = self.visit(ctx.expr())
        
        if not isinstance(condition, bool):
            self.type_errors.append(f"Type error: If condition must be boolean, got {type(condition).__name__}")
            return None
            
        if condition:
            self.visit(ctx.statement(0)) 
        else:
            self.visit(ctx.statement(1)) 
            
        return None
        
    def visitWhileStatement(self, ctx):
        max_iterations = 1000 
        iteration_count = 0
        
        while iteration_count < max_iterations:
            condition = self.visit(ctx.expr())
            
            if not isinstance(condition, bool):
                self.type_errors.append(f"Type error: While condition must be boolean, got {type(condition).__name__}")
                return None
                
            if not condition:
                break
                
            self.visit(ctx.statement())

            iteration_count += 1
        
        if iteration_count >= max_iterations:
            self.type_errors.append(f"Warning: While loop reached maximum iteration limit ({max_iterations}), possible infinite loop")
                
        return None
        
    def visitIntType(self, ctx):
        return 'int'

    def visitFloatType(self, ctx):
        return 'float'

    def visitBoolType(self, ctx):
        return 'bool'

    def visitStringType(self, ctx):
        return 'string'

    def visitFileType(self, ctx):
        return 'FILE'
        
    def visitExprStatement(self, ctx):
        return self.visit(ctx.expr())
        
    def visitMulDivMod(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        
        if isinstance(left, int) and isinstance(right, float):
            left = float(left)
        elif isinstance(left, float) and isinstance(right, int):
            right = float(right)
        
        if op == '%':
            if not (isinstance(left, int) and isinstance(right, int)):
                self.type_errors.append(f"Type error: '%' operator requires integer operands, got {type(left).__name__} and {type(right).__name__}")
                return None
        else:
            if not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
                self.type_errors.append(f"Type error: '{op}' operator requires numeric operands, got {type(left).__name__} and {type(right).__name__}")
                return None
            
        if op == '*':
            return left * right
        elif op == '/':
            if right == 0:
                self.type_errors.append("Runtime error: Division by zero")
                return None
                
            if isinstance(left, int) and isinstance(right, int):
                return left // right
            else:
                return left / right
        elif op == '%':
            if right == 0:
                self.type_errors.append("Runtime error: Modulo by zero")
                return None
            return left % right
            
    def visitAddSubConcat(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        
        if op in ['+', '-'] and isinstance(left, int) and isinstance(right, float):
            left = float(left)
        elif op in ['+', '-'] and isinstance(left, float) and isinstance(right, int):
            right = float(right)
        
        if op == '.':
            if not (isinstance(left, str) and isinstance(right, str)):
                self.type_errors.append(f"Type error: '.' operator requires string operands, got {type(left).__name__} and {type(right).__name__}")
                return None
            return left + right
        elif op == '+':
            if isinstance(left, str) and isinstance(right, str):
                return left + right
            elif not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
                self.type_errors.append(f"Type error: '{op}' operator requires numeric operands, got {type(left).__name__} and {type(right).__name__}")
                return None
            return left + right
        else:  
            if not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
                self.type_errors.append(f"Type error: '{op}' operator requires numeric operands, got {type(left).__name__} and {type(right).__name__}")
                return None
            return left - right
            
    def visitRelational(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        
        if isinstance(left, int) and isinstance(right, float):
            left = float(left)
        elif isinstance(left, float) and isinstance(right, int):
            right = float(right)
        
        if not ((isinstance(left, int) and isinstance(right, int)) or 
                (isinstance(left, float) and isinstance(right, float))):
            self.type_errors.append(f"Type error: '{op}' operator requires numeric operands of the same type, got {type(left).__name__} and {type(right).__name__}")
            return None
            
        if op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '<=':
            return left <= right
        elif op == '>=':
            return left >= right
            
    def visitEquality(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        
        if type(left) != type(right) and not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
            self.type_errors.append(f"Type error: Cannot compare {type(left).__name__} and {type(right).__name__}")
            return None
        
        if op == '==':
            return left == right
        else: 
            return left != right
            
    def visitLogicalAnd(self, ctx):
        left = self.visit(ctx.expr(0))
        
        if not isinstance(left, bool):
            self.type_errors.append(f"Type error: '&&' operator requires boolean operands, got {type(left).__name__}")
            return None
            
        if not left:
            return False
            
        right = self.visit(ctx.expr(1))
        
        if not isinstance(right, bool):
            self.type_errors.append(f"Type error: '&&' operator requires boolean operands, got {type(right).__name__}")
            return None
            
        return left and right
            
    def visitLogicalOr(self, ctx):
        left = self.visit(ctx.expr(0))
        
        if not isinstance(left, bool):
            self.type_errors.append(f"Type error: '||' operator requires boolean operands, got {type(left).__name__}")
            return None
            
        if left:
            return True
            
        right = self.visit(ctx.expr(1))
        
        if not isinstance(right, bool):
            self.type_errors.append(f"Type error: '||' operator requires boolean operands, got {type(right).__name__}")
            return None
            
        return left or right
        
    def visitLogicalNot(self, ctx):
        value = self.visit(ctx.expr())
        
        if not isinstance(value, bool):
            try:
                value = bool(value)
            except:
                self.type_errors.append(f"Type error: '!' operator requires boolean operand, got {type(value).__name__}")
                return None
        
        return not value
            
    def visitNotOp(self, ctx):
        operand = self.visit(ctx.expr())

        if not isinstance(operand, bool):
            self.type_errors.append(f"Type error: '!' operator requires boolean operand, got {type(operand).__name__}")
            return None
            
        return not operand
            
    def visitIntLiteral(self, ctx):
        return int(ctx.INT().getText())
        
    def visitFloatLiteral(self, ctx):
        return float(ctx.FLOAT().getText())
        
    def visitBoolLiteral(self, ctx):
        text = ctx.BOOL().getText()
        return text == 'true'
        
    def visitStringLiteral(self, ctx):
        text = ctx.STRING().getText()
        text = text[1:-1]
        text = text.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\\\\', '\\')
        return text
        
    def visitVariable(self, ctx):
        id_name = ctx.ID().getText()
        
        if id_name not in self.declared:
            self.type_errors.append(f"Variable '{id_name}' used before declaration")
            return None
        
        value = self.memory.get(id_name)
        
        return value
        
    def visitParens(self, ctx):
        return self.visit(ctx.expr())
        
    def _check_type_compatibility(self, value, expected_type):
        """
        Kontroluje, zda je hodnota kompatibilní s očekávaným typem
        """
        if expected_type == 'int':
            return isinstance(value, int)
        elif expected_type == 'float':
            return isinstance(value, (float, int))
        elif expected_type == 'bool':
            return isinstance(value, bool)
        elif expected_type == 'string':
            return isinstance(value, str)
        else:
            return False

    def visitId(self, ctx):
        id_name = ctx.getText()
        
        if id_name not in self.declared:
            self.type_errors.append(f"Variable '{id_name}' used before declaration")
            return None
            
        return self.memory.get(id_name, self._get_default_value(self.types[id_name]))

    def visitVarDeclaration(self, ctx):
        """
        Zpracovává deklaraci proměnné, ukládá typ a inicializuje hodnotu
        """
        var_type = ctx.type_().getText()
        var_name = ctx.ID().getText()
        
        if var_name in self.declared:
            return self.memory.get(var_name)
        
        self.declared.add(var_name)
        self.types[var_name] = var_type
        
        if ctx.expr():
            value = self.visit(ctx.expr())
            
            if not self._check_type_compatibility(value, var_type):
                self.type_errors.append(f"Type error: Cannot assign {type(value).__name__} to variable '{var_name}' of type {var_type}")
                return None
                
            self.memory[var_name] = value
        else:
            self.memory[var_name] = self._get_default_value(var_type)
        
        return self.memory[var_name]

    def _get_default_value(self, type_name):
        """Vrací výchozí hodnotu pro daný typ proměnné"""
        if type_name == 'int':
            return 0
        elif type_name == 'float':
            return 0.0
        elif type_name == 'bool':
            return False
        elif type_name == 'string':
            return ""
        else:
            self.type_errors.append(f"Unknown type: {type_name}")
            return None

    def visitUnaryMinus(self, ctx):
        value = self.visit(ctx.expr())
        
        if not isinstance(value, (int, float)):
            self.type_errors.append(f"Type error: Unary '-' operator requires numeric operand, got {type(value).__name__}")
            return None
            
        return -value

    def visitShiftLeft(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        # Pokud left je FILE proměnná
        if isinstance(left, str) and left in self.memory and self.types.get(left) == 'FILE':
            filename = self.memory[left]
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(str(right) + '\n')
            return filename
        # Pokud left je literál souboru (string končící na .txt)
        elif isinstance(left, str) and left.endswith('.txt'):
            with open(left, 'a', encoding='utf-8') as f:
                f.write(str(right) + '\n')
            return left
        else:
            self.type_errors.append("Operator '<<' vyžaduje jako levý operand soubor (FILE) nebo název souboru (string končící na .txt)")
            return None