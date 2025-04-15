from ExprVisitor import ExprVisitor
from ExprParser import ExprParser
import sys

class EvalVisitor(ExprVisitor):
    def __init__(self):
        self.memory = {}   # Store variable values
        self.types = {}    # Store variable types
        self.declared = set()  # Track declared variables
        self.type_errors = []
        
    def visitProg(self, ctx):
        results = []
        for cmd in ctx.command():
            result = self.visit(cmd)
            if result is not None:
                results.append(result)
        return results
        
    def visitCommand(self, ctx):
        return self.visit(ctx.statement())
    
    def visitEmptyStatement(self, ctx):
        # Empty statement does nothing and returns nothing
        return None
        
    def visitAssignment(self, ctx):
        id_name = ctx.ID().getText()
        
        # Check if variable is declared
        if id_name not in self.declared:
            self.type_errors.append(f"Variable '{id_name}' used before declaration")
            return None
            
        value = self.visit(ctx.expr())
        
        # Type checking
        expected_type = self.types[id_name]
        if not self._check_type_compatibility(value, expected_type):
            self.type_errors.append(f"Type error: Cannot assign {type(value).__name__} to variable '{id_name}' of type {expected_type}")
            return None
            
        # Store value
        self.memory[id_name] = value
        
        # Odstranit debug výpisy
        # print(f"Assignment: {id_name} = {value}")
        # print(f"Memory after assignment: {self.memory}")
        
        return value  # Assignment returns the assigned value
        
    def visitDeclaration(self, ctx):
        type_name = self.visit(ctx.type_())
        
        # Process each variable in the declaration
        for id_node in ctx.ID():
            id_name = id_node.getText()
            
            # Check for redeclaration
            if id_name in self.declared:
                self.type_errors.append(f"Variable '{id_name}' already declared")
                continue
                
            # Register the variable
            self.declared.add(id_name)
            self.types[id_name] = type_name
            
            # Set default value based on type
            if type_name == 'int':
                self.memory[id_name] = 0
            elif type_name == 'float':
                self.memory[id_name] = 0.0
            elif type_name == 'bool':
                self.memory[id_name] = False
            elif type_name == 'string':
                self.memory[id_name] = ""
                
        return None
        
    def visitDeclarationWithAssignment(self, ctx):
        id_name = ctx.ID().getText()
        type_name = self.visit(ctx.type_())
        
        # Check for redeclaration
        if id_name in self.declared:
            self.type_errors.append(f"Variable '{id_name}' already declared")
            return None
            
        # Register the variable
        self.declared.add(id_name)
        self.types[id_name] = type_name
        
        # Set value from expression
        value = self.visit(ctx.expr())
        
        # Type checking
        if not self._check_type_compatibility(value, type_name):
            self.type_errors.append(f"Type error: Cannot assign {type(value).__name__} to variable '{id_name}' of type {type_name}")
            # Set default value instead
            if type_name == 'int':
                self.memory[id_name] = 0
            elif type_name == 'float':
                self.memory[id_name] = 0.0
            elif type_name == 'bool':
                self.memory[id_name] = False
            elif type_name == 'string':
                self.memory[id_name] = ""
        else:
            # Value is compatible, store it
            self.memory[id_name] = value
            
        return None
    
    def visitReadStatement(self, ctx):
        # Process each variable in the read statement
        for id_node in ctx.ID():
            id_name = id_node.getText()
            
            # Check if variable is declared
            if id_name not in self.declared:
                self.type_errors.append(f"Variable '{id_name}' used before declaration")
                continue
                
            # Get the type of the variable
            var_type = self.types[id_name]
            
            # Read input from user
            try:
                input_value = input(f"Enter value for {id_name} ({var_type}): ")
                
                # Convert input to appropriate type
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
                    
                # Store the value
                self.memory[id_name] = value
                    
            except ValueError:
                self.type_errors.append(f"Invalid input for variable '{id_name}' of type {var_type}")
                
        return None
        
    def visitWriteStatement(self, ctx):
        # Evaluate and print each expression
        values = []
        for expr_ctx in ctx.expr():
            value = self.visit(expr_ctx)
            values.append(value)
            
        # Print values separated by spaces, with newline at the end
        print(" ".join(str(val) for val in values))
        
        return None
        
    def visitBlockStatement(self, ctx):
        # Execute each statement in the block
        for stmt_ctx in ctx.statement():
            self.visit(stmt_ctx)
            
        return None
        
    def visitIfStatement(self, ctx):
        # Evaluate condition
        condition = self.visit(ctx.expr())
        
        # Type checking for condition
        if not isinstance(condition, bool):
            self.type_errors.append(f"Type error: If condition must be boolean, got {type(condition).__name__}")
            return None
            
        # Execute statement if condition is true
        if condition:
            self.visit(ctx.statement())
            
        return None
        
    def visitIfElseStatement(self, ctx):
        # Evaluate condition
        condition = self.visit(ctx.expr())
        
        # Type checking for condition
        if not isinstance(condition, bool):
            self.type_errors.append(f"Type error: If condition must be boolean, got {type(condition).__name__}")
            return None
            
        # Execute appropriate branch based on condition
        if condition:
            self.visit(ctx.statement(0))  # First statement (if branch)
        else:
            self.visit(ctx.statement(1))  # Second statement (else branch)
            
        return None
        
    def visitWhileStatement(self, ctx):
        max_iterations = 1000  # Bezpečnostní limit iterací
        iteration_count = 0
        
        while iteration_count < max_iterations:
            # Evaluate condition
            condition = self.visit(ctx.expr())
            
            # Odstranit debug výpis
            # print(f"While condition evaluated to: {condition}, iteration: {iteration_count}")
            
            # Type checking for condition
            if not isinstance(condition, bool):
                self.type_errors.append(f"Type error: While condition must be boolean, got {type(condition).__name__}")
                return None
                
            # Exit loop if condition is false
            if not condition:
                break
                
            # Execute statement body
            self.visit(ctx.statement())
            
            # Odstranit debug výpis
            # print(f"While loop memory after iteration {iteration_count}: {self.memory}")
            
            # Increment counter to prevent infinite loops
            iteration_count += 1
        
        # Varování, pokud jsme dosáhli limitu iterací
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
        
    def visitExprStatement(self, ctx):
        return self.visit(ctx.expr())
        
    # Arithmetic operations
    def visitMulDivMod(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        
        # Type conversion for int to float if needed
        if isinstance(left, int) and isinstance(right, float):
            left = float(left)
        elif isinstance(left, float) and isinstance(right, int):
            right = float(right)
        
        # Type checking
        if op == '%':
            # Modulo only works on integers
            if not (isinstance(left, int) and isinstance(right, int)):
                self.type_errors.append(f"Type error: '%' operator requires integer operands, got {type(left).__name__} and {type(right).__name__}")
                return None
        else:
            # Multiplication and division require numeric operands
            if not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
                self.type_errors.append(f"Type error: '{op}' operator requires numeric operands, got {type(left).__name__} and {type(right).__name__}")
                return None
            
        if op == '*':
            return left * right
        elif op == '/':
            if right == 0:
                self.type_errors.append("Runtime error: Division by zero")
                return None
                
            # Division between integers produces int result (integer division)
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
        
        # Odstranit debug výpis
        # print(f"AddSubConcat operation: {left} {op} {right}")
        
        # Type conversion for int to float if needed
        if op in ['+', '-'] and isinstance(left, int) and isinstance(right, float):
            left = float(left)
        elif op in ['+', '-'] and isinstance(left, float) and isinstance(right, int):
            right = float(right)
        
        # Type checking based on operator
        if op == '.':
            # String concatenation
            if not (isinstance(left, str) and isinstance(right, str)):
                self.type_errors.append(f"Type error: '.' operator requires string operands, got {type(left).__name__} and {type(right).__name__}")
                return None
            return left + right
        elif op == '+':
            # Addition requires numeric operands or string concatenation
            if isinstance(left, str) and isinstance(right, str):
                return left + right
            elif not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
                self.type_errors.append(f"Type error: '{op}' operator requires numeric operands, got {type(left).__name__} and {type(right).__name__}")
                return None
            return left + right
        else:  # op == '-'
            # Subtraction requires numeric operands
            if not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
                self.type_errors.append(f"Type error: '{op}' operator requires numeric operands, got {type(left).__name__} and {type(right).__name__}")
                return None
            return left - right
            
    def visitRelational(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        
        # Type conversion for int to float if needed
        if isinstance(left, int) and isinstance(right, float):
            left = float(left)
        elif isinstance(left, float) and isinstance(right, int):
            right = float(right)
        
        # Type checking for relational operators
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
        
        # Type conversion for int to float if needed
        if isinstance(left, int) and isinstance(right, float):
            left = float(left)
        elif isinstance(left, float) and isinstance(right, int):
            right = float(right)
        
        # Type checking for equality operators
        # Allow equality/inequality for all types, but operands must be comparable
        allowed_types = (int, float, str)
        if not (type(left) == type(right) or 
                (isinstance(left, allowed_types) and isinstance(right, allowed_types))):
            self.type_errors.append(f"Type error: Cannot compare {type(left).__name__} and {type(right).__name__} with operator '{op}'")
            return None
            
        if op == '==':
            return left == right
        else:  # op == '!='
            return left != right
            
    def visitLogicalAnd(self, ctx):
        left = self.visit(ctx.expr(0))
        
        # Type checking for left operand
        if not isinstance(left, bool):
            self.type_errors.append(f"Type error: '&&' operator requires boolean operands, got {type(left).__name__}")
            return None
            
        # Short-circuit evaluation
        if not left:
            return False
            
        # Evaluate right operand
        right = self.visit(ctx.expr(1))
        
        # Type checking for right operand
        if not isinstance(right, bool):
            self.type_errors.append(f"Type error: '&&' operator requires boolean operands, got {type(right).__name__}")
            return None
            
        return left and right
            
    def visitLogicalOr(self, ctx):
        left = self.visit(ctx.expr(0))
        
        # Type checking for left operand
        if not isinstance(left, bool):
            self.type_errors.append(f"Type error: '||' operator requires boolean operands, got {type(left).__name__}")
            return None
            
        # Short-circuit evaluation
        if left:
            return True
            
        # Evaluate right operand
        right = self.visit(ctx.expr(1))
        
        # Type checking for right operand
        if not isinstance(right, bool):
            self.type_errors.append(f"Type error: '||' operator requires boolean operands, got {type(right).__name__}")
            return None
            
        return left or right
            
    def visitNotOp(self, ctx):
        operand = self.visit(ctx.expr())
        
        # Type checking
        if not isinstance(operand, bool):
            error_msg = f"Type error: '!' operator requires boolean operand, got {type(operand).__name__}"
            self.type_errors.append(error_msg)
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
        # Remove quotes and handle escape sequences
        text = ctx.STRING().getText()
        # Remove the surrounding quotes
        text = text[1:-1]
        # Handle escape sequences (basic implementation)
        text = text.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\\\\', '\\')
        return text
        
    def visitVariable(self, ctx):
        id_name = ctx.ID().getText()
        
        # Check if variable is declared
        if id_name not in self.declared:
            self.type_errors.append(f"Variable '{id_name}' used before declaration")
            return None
        
        # Get current value from memory (odstranit debug výpis)
        value = self.memory.get(id_name)
        # print(f"Variable access: {id_name} = {value}")  # Odstranit tento řádek
        
        return value
        
    def visitParens(self, ctx):
        return self.visit(ctx.expr())
        
    def _check_type_compatibility(self, value, expected_type):
        """Check if a value is compatible with the expected type."""
        if expected_type == 'int':
            return isinstance(value, int)
        elif expected_type == 'float':
            # Allow int to float conversion
            return isinstance(value, (int, float))
        elif expected_type == 'bool':
            return isinstance(value, bool)
        elif expected_type == 'string':
            return isinstance(value, str)
        return False

    def visitId(self, ctx):
        id_name = ctx.getText()
        
        # Check if variable is declared
        if id_name not in self.declared:
            self.type_errors.append(f"Variable '{id_name}' used before declaration")
            return None
            
        # Return the variable value from memory
        return self.memory.get(id_name, self._get_default_value(self.types[id_name]))

    def visitProgram(self, ctx):
        """
        Hlavní metoda pro návštěvu programu - zpracovává jednotlivé příkazy sekvenčně
        """
        results = []
        
        # Process each statement in the program
        for statement in ctx.statement():
            result = self.visit(statement)
            # Store non-None results
            if result is not None:
                results.append(result)
                
        return results

    def visitVarDeclaration(self, ctx):
        """
        Zpracovává deklaraci proměnné, ukládá typ a inicializuje hodnotu
        """
        var_type = ctx.type_().getText()
        var_name = ctx.ID().getText()
        
        # Check if variable is already declared
        if var_name in self.declared:
            # Skip re-declaration if this happens in a loop (just return current value)
            return self.memory.get(var_name)
        
        # Declare the variable - mark as declared and set its type
        self.declared.add(var_name)
        self.types[var_name] = var_type
        
        # Initialize with value if assignment is present
        if ctx.expr():
            value = self.visit(ctx.expr())
            
            # Type checking for initial value
            if not self._check_type_compatibility(value, var_type):
                self.type_errors.append(f"Type error: Cannot assign {type(value).__name__} to variable '{var_name}' of type {var_type}")
                return None
                
            self.memory[var_name] = value
        else:
            # Initialize with default value if no assignment
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
        
        # Type checking
        if not isinstance(value, (int, float)):
            self.type_errors.append(f"Type error: Unary '-' operator requires numeric operand, got {type(value).__name__}")
            return None
            
        # Zde je pravděpodobně problém - místo -value je použito value
        return -value  # Ujistěte se, že vracíte -value, ne value nebo abs(value)