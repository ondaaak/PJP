from ExprListener import ExprListener

class EvalListener(ExprListener):
    def __init__(self):
        self.values = {}  # Store variable values
        self.types = {}   # Store variable types
        self.errors = []  # Store errors
        self.stack = []   # Evaluation stack
        
    def exitAssignment(self, ctx):
        id_name = ctx.ID().getText()
        if self.stack:
            value = self.stack[-1]  # Peek at the top of the stack
            self.values[id_name] = value
            
            # Infer type
            if isinstance(value, int):
                self.types[id_name] = 'int'
            elif isinstance(value, float):
                self.types[id_name] = 'float'
            elif isinstance(value, bool):
                self.types[id_name] = 'bool'
            elif isinstance(value, str):
                self.types[id_name] = 'string'
        
    def exitExprStatement(self, ctx):
        # Result is already on the stack
        pass
        
    def exitMulDiv(self, ctx):
        if len(self.stack) < 2:
            return
            
        right = self.stack.pop()
        left = self.stack.pop()
        
        # Type checking
        if not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
            self.errors.append(f"Type error: '{ctx.op.text}' requires numeric operands")
            return
            
        if ctx.op.text == '*':
            self.stack.append(left * right)
        elif ctx.op.text == '/':
            if right == 0:
                self.errors.append("Runtime error: Division by zero")
                return
                
            # Integer division for int/int, float division otherwise
            if isinstance(left, int) and isinstance(right, int):
                self.stack.append(left // right)
            else:
                self.stack.append(left / right)
            
    def exitAddSub(self, ctx):
        if len(self.stack) < 2:
            return
            
        right = self.stack.pop()
        left = self.stack.pop()
        
        # Special case for string concatenation
        if ctx.op.text == '+' and isinstance(left, str) and isinstance(right, str):
            self.stack.append(left + right)
            return
            
        # Type checking for numeric operations
        if not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
            self.errors.append(f"Type error: '{ctx.op.text}' requires numeric operands")
            return
            
        if ctx.op.text == '+':
            self.stack.append(left + right)
        elif ctx.op.text == '-':
            self.stack.append(left - right)
            
    def exitIntLiteral(self, ctx):
        self.stack.append(int(ctx.INT().getText()))
        
    def exitFloatLiteral(self, ctx):
        self.stack.append(float(ctx.FLOAT().getText()))
        
    def exitBoolLiteral(self, ctx):
        text = ctx.BOOL().getText()
        self.stack.append(text == 'true')
        
    def exitStringLiteral(self, ctx):
        # Remove quotes and handle escape sequences
        text = ctx.STRING().getText()
        # Remove the surrounding quotes
        text = text[1:-1]
        # Handle escape sequences (basic implementation)
        text = text.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\\\\', '\\')
        self.stack.append(text)
        
    def exitVariable(self, ctx):
        id_name = ctx.ID().getText()
        if id_name not in self.values:
            self.errors.append(f"Variable '{id_name}' is not defined")
            return
        self.stack.append(self.values[id_name])
        
    def exitParens(self, ctx):
        # Result already on the stack
        pass