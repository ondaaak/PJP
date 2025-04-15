from ExprListener import ExprListener

class EvalListener(ExprListener):
    def __init__(self):
        self.values = {}      # Store variable values
        self.types = {}       # Store variable types
        self.declared = set() # Track declared variables
        self.errors = []      # Store errors
        self.stack = []       # Evaluation stack
        self.current_type = None  # Used during type processing
        
    def exitAssignment(self, ctx):
        id_name = ctx.ID().getText()
        
        # Check if variable is declared
        if id_name not in self.declared:
            self.errors.append(f"Variable '{id_name}' used before declaration")
            return
            
        # Get value from stack
        if self.stack:
            value = self.stack.pop()
            
            # Type checking
            expected_type = self.types[id_name]
            if not self._check_type_compatibility(value, expected_type):
                self.errors.append(f"Type error: Cannot assign {type(value).__name__} to variable '{id_name}' of type {expected_type}")
                return
                
            # Store value
            self.values[id_name] = value
        
    def exitDeclaration(self, ctx):
        id_name = ctx.ID().getText()
        
        # Check for redeclaration
        if id_name in self.declared:
            self.errors.append(f"Variable '{id_name}' already declared")
            return
        
        # Get type directly from context
        type_ctx = ctx.type_()
        if type_ctx.getChildCount() > 0:
            type_text = type_ctx.getChild(0).getText()
            
            # Set type based on text
            if type_text == 'int':
                type_name = 'int'
            elif type_text == 'float':
                type_name = 'float'
            elif type_text == 'bool':
                type_name = 'bool'
            elif type_text == 'string':
                type_name = 'string'
            else:
                type_name = 'unknown'
                
            # Register the variable
            self.declared.add(id_name)
            self.types[id_name] = type_name
            
            # Set default value based on type
            if type_name == 'int':
                self.values[id_name] = 0
            elif type_name == 'float':
                self.values[id_name] = 0.0
            elif type_name == 'bool':
                self.values[id_name] = False
            elif type_name == 'string':
                self.values[id_name] = ""
        
    def exitDeclarationWithAssignment(self, ctx):
        id_name = ctx.ID().getText()
        
        # Check for redeclaration
        if id_name in self.declared:
            self.errors.append(f"Variable '{id_name}' already declared")
            return
            
        # Get type directly from context
        type_ctx = ctx.type_()
        if type_ctx.getChildCount() > 0:
            type_text = type_ctx.getChild(0).getText()
            
            # Set type based on text
            if type_text == 'int':
                type_name = 'int'
            elif type_text == 'float':
                type_name = 'float'
            elif type_text == 'bool':
                type_name = 'bool'
            elif type_text == 'string':
                type_name = 'string'
            else:
                type_name = 'unknown'
                
            # Register the variable
            self.declared.add(id_name)
            self.types[id_name] = type_name
            
            # Get value from stack
            if self.stack:
                value = self.stack.pop()
                
                # Type checking
                if not self._check_type_compatibility(value, type_name):
                    self.errors.append(f"Type error: Cannot assign {type(value).__name__} to variable '{id_name}' of type {type_name}")
                    # Set default value instead
                    if type_name == 'int':
                        self.values[id_name] = 0
                    elif type_name == 'float':
                        self.values[id_name] = 0.0
                    elif type_name == 'bool':
                        self.values[id_name] = False
                    elif type_name == 'string':
                        self.values[id_name] = ""
                else:
                    # Value is compatible, store it
                    self.values[id_name] = value
        
    def exitIntType(self, ctx):
        self.current_type = 'int'
        
    def exitFloatType(self, ctx):
        self.current_type = 'float'
        
    def exitBoolType(self, ctx):
        self.current_type = 'bool'
        
    def exitStringType(self, ctx):
        self.current_type = 'string'
        
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
        
        # Check if variable is declared
        if id_name not in self.declared:
            self.errors.append(f"Variable '{id_name}' used before declaration")
            return
            
        self.stack.append(self.values[id_name])
        
    def exitParens(self, ctx):
        # Result already on the stack
        pass
        
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