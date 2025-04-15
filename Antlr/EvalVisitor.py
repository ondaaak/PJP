from ExprVisitor import ExprVisitor
from ExprParser import ExprParser

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
        id_name = ctx.ID().getText()
        # Fix: use type_ instead of type
        type_name = self.visit(ctx.type_())
        
        # Check for redeclaration
        if id_name in self.declared:
            self.type_errors.append(f"Variable '{id_name}' already declared")
            return None
            
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
        # Fix: use type_ instead of type
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