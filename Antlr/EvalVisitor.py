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
        return None  # Assignment doesn't return a value
        
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
        while True:
            # Evaluate condition
            condition = self.visit(ctx.expr())
            
            # Type checking for condition
            if not isinstance(condition, bool):
                self.type_errors.append(f"Type error: While condition must be boolean, got {type(condition).__name__}")
                return None
                
            # Exit loop if condition is false
            if not condition:
                break
                
            # Execute statement body
            self.visit(ctx.statement())
            
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
        
    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        # Type checking
        if not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
            error_msg = f"Type error: '{ctx.op.text}' operator requires numeric operands, got {type(left).__name__} and {type(right).__name__}"
            self.type_errors.append(error_msg)
            return None
            
        if ctx.op.text == '*':
            return left * right
        else:  # Division
            if right == 0:
                self.type_errors.append("Runtime error: Division by zero")
                return None
                
            # Integer division for int/int, float division otherwise
            if isinstance(left, int) and isinstance(right, int):
                return left // right
            else:
                return left / right
            
    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        # Special case for string concatenation
        if ctx.op.text == '+' and isinstance(left, str) and isinstance(right, str):
            return left + right
            
        # Type checking for numeric operations
        if not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
            error_msg = f"Type error: '{ctx.op.text}' operator requires numeric operands, got {type(left).__name__} and {type(right).__name__}"
            self.type_errors.append(error_msg)
            return None
            
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right
            
    def visitComparison(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        # Check that types are comparable
        if type(left) != type(right) and not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
            error_msg = f"Type error: Cannot compare {type(left).__name__} and {type(right).__name__} with operator '{ctx.op.text}'"
            self.type_errors.append(error_msg)
            return None
            
        # Perform comparison
        if ctx.op.text == '<':
            return left < right
        elif ctx.op.text == '>':
            return left > right
        elif ctx.op.text == '<=':
            return left <= right
        elif ctx.op.text == '>=':
            return left >= right
        elif ctx.op.text == '==':
            return left == right
        elif ctx.op.text == '!=':
            return left != right
            
    def visitLogicalOp(self, ctx):
        left = self.visit(ctx.expr(0))
        
        # Type checking for left operand
        if not isinstance(left, bool):
            error_msg = f"Type error: '{ctx.op.text}' operator requires boolean operands, got {type(left).__name__}"
            self.type_errors.append(error_msg)
            return None
            
        # Short-circuit evaluation
        if ctx.op.text == '&&' and not left:
            return False
        elif ctx.op.text == '||' and left:
            return True
            
        # Evaluate right operand if needed
        right = self.visit(ctx.expr(1))
        
        # Type checking for right operand
        if not isinstance(right, bool):
            error_msg = f"Type error: '{ctx.op.text}' operator requires boolean operands, got {type(right).__name__}"
            self.type_errors.append(error_msg)
            return None
            
        # Perform logical operation
        if ctx.op.text == '&&':
            return left and right
        elif ctx.op.text == '||':
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
            
        return self.memory[id_name]
        
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