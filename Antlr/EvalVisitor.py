from ExprVisitor import ExprVisitor
from ExprParser import ExprParser

class EvalVisitor(ExprVisitor):
    def __init__(self):
        self.memory = {}  # Store variable values
        self.types = {}   # Store variable types
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
        value = self.visit(ctx.expr())
        
        if value is not None:
            self.memory[id_name] = value
            # Infer type based on value
            if isinstance(value, int):
                self.types[id_name] = 'int'
            elif isinstance(value, float):
                self.types[id_name] = 'float'
            elif isinstance(value, bool):
                self.types[id_name] = 'bool'
            elif isinstance(value, str):
                self.types[id_name] = 'string'
        
        return None  # Assignment doesn't return a value
        
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
        if id_name not in self.memory:
            self.type_errors.append(f"Variable '{id_name}' is not defined")
            return None
        return self.memory[id_name]
        
    def visitParens(self, ctx):
        return self.visit(ctx.expr())