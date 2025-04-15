from ExprListener import ExprListener

class EvalListener(ExprListener):
    def __init__(self):
        self.values = {}      # Store variable values
        self.types = {}       # Store variable types
        self.declared = set() # Track declared variables
        self.errors = []      # Store errors
        self.stack = []       # Evaluation stack
        self.current_scope = []  # Track block scopes
        
    # Empty Statement
    def exitEmptyStatement(self, ctx):
        # Nothing to do for empty statement
        pass
        
    # Assignment
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
        
    # Declaration
    def exitDeclaration(self, ctx):
        # Get type directly from context
        type_ctx = ctx.type_()
        if type_ctx.getChildCount() > 0:
            type_text = type_ctx.getChild(0).getText()
            
            # Process each variable in the declaration
            for id_node in ctx.ID():
                id_name = id_node.getText()
                
                # Check for redeclaration
                if id_name in self.declared:
                    self.errors.append(f"Variable '{id_name}' already declared")
                    continue
                    
                # Register the variable
                self.declared.add(id_name)
                self.types[id_name] = type_text
                
                # Set default value based on type
                if type_text == 'int':
                    self.values[id_name] = 0
                elif type_text == 'float':
                    self.values[id_name] = 0.0
                elif type_text == 'bool':
                    self.values[id_name] = False
                elif type_text == 'string':
                    self.values[id_name] = ""
        
    # Declaration with Assignment
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
            
            # Register the variable
            self.declared.add(id_name)
            self.types[id_name] = type_text
            
            # Get value from stack
            if self.stack:
                value = self.stack.pop()
                
                # Type checking
                if not self._check_type_compatibility(value, type_text):
                    self.errors.append(f"Type error: Cannot assign {type(value).__name__} to variable '{id_name}' of type {type_text}")
                    # Set default value instead
                    if type_text == 'int':
                        self.values[id_name] = 0
                    elif type_text == 'float':
                        self.values[id_name] = 0.0
                    elif type_text == 'bool':
                        self.values[id_name] = False
                    elif type_text == 'string':
                        self.values[id_name] = ""
                else:
                    # Value is compatible, store it
                    self.values[id_name] = value
    
    # Read Statement
    def exitReadStatement(self, ctx):
        # Process each variable in the read statement
        for id_node in ctx.ID():
            id_name = id_node.getText()
            
            # Check if variable is declared
            if id_name not in self.declared:
                self.errors.append(f"Variable '{id_name}' used before declaration")
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
                        self.errors.append(f"Invalid boolean value for variable '{id_name}': {input_value}")
                        continue
                elif var_type == 'string':
                    value = input_value
                else:
                    self.errors.append(f"Unknown type for variable '{id_name}': {var_type}")
                    continue
                    
                # Store the value
                self.values[id_name] = value
                    
            except ValueError:
                self.errors.append(f"Invalid input for variable '{id_name}' of type {var_type}")
    
    # Write Statement
    def exitWriteStatement(self, ctx):
        # For write statements, we evaluate expressions and then print them
        expressions = []
        # For each expression in the write statement, peek at the stack
        # We'll read them in reverse order since they were pushed in order
        expr_count = len(ctx.expr())
        for i in range(expr_count):
            if len(self.stack) > 0:
                value = self.stack.pop()
                expressions.insert(0, value)  # Insert at beginning to reverse order
                
        # Print the expressions
        print(" ".join(str(expr) for expr in expressions))
    
    # Block Statement
    def exitBlockStatement(self, ctx):
        # No specific processing needed at block exit, statements were already executed
        pass
    
    # If Statement
    def exitIfStatement(self, ctx):
        # The condition has been evaluated and is on the stack
        if self.stack and len(self.stack) > 0:
            condition = self.stack.pop()
            
            # Type checking for condition
            if not isinstance(condition, bool):
                self.errors.append(f"Type error: If condition must be boolean, got {type(condition).__name__}")
    
    # If-Else Statement
    def exitIfElseStatement(self, ctx):
        # Similar to If Statement, condition was already evaluated
        if self.stack and len(self.stack) > 0:
            condition = self.stack.pop()
            
            # Type checking for condition
            if not isinstance(condition, bool):
                self.errors.append(f"Type error: If condition must be boolean, got {type(condition).__name__}")
    
    # While Statement
    def exitWhileStatement(self, ctx):
        # The listener only examines the parse tree, doesn't execute loops
        # So we just type-check the condition
        if self.stack and len(self.stack) > 0:
            condition = self.stack.pop()
            
            # Type checking for condition
            if not isinstance(condition, bool):
                self.errors.append(f"Type error: While condition must be boolean, got {type(condition).__name__}")
    
    # Expression Statement
    def exitExprStatement(self, ctx):
        # For an expression statement, we evaluate but don't need to do anything with the result
        # The result is on the stack, but we'll leave it there
        pass
        
    # Type Handling
    def exitIntType(self, ctx):
        # Not needed in listener
        pass
        
    def exitFloatType(self, ctx):
        # Not needed in listener
        pass
        
    def exitBoolType(self, ctx):
        # Not needed in listener
        pass
        
    def exitStringType(self, ctx):
        # Not needed in listener
        pass
    
    # Expressions
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
            
    def exitComparison(self, ctx):
        if len(self.stack) < 2:
            return
            
        right = self.stack.pop()
        left = self.stack.pop()
        
        # Check that types are comparable
        if type(left) != type(right) and not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
            self.errors.append(f"Type error: Cannot compare {type(left).__name__} and {type(right).__name__} with operator '{ctx.op.text}'")
            return
            
        # Perform comparison
        if ctx.op.text == '<':
            self.stack.append(left < right)
        elif ctx.op.text == '>':
            self.stack.append(left > right)
        elif ctx.op.text == '<=':
            self.stack.append(left <= right)
        elif ctx.op.text == '>=':
            self.stack.append(left >= right)
        elif ctx.op.text == '==':
            self.stack.append(left == right)
        elif ctx.op.text == '!=':
            self.stack.append(left != right)
            
    def exitLogicalOp(self, ctx):
        if len(self.stack) < 2:
            return
            
        right = self.stack.pop()
        left = self.stack.pop()
        
        # Type checking
        if not (isinstance(left, bool) and isinstance(right, bool)):
            self.errors.append(f"Type error: '{ctx.op.text}' requires boolean operands")
            return
            
        if ctx.op.text == '&&':
            self.stack.append(left and right)
        elif ctx.op.text == '||':
            self.stack.append(left or right)
            
    def exitNotOp(self, ctx):
        if len(self.stack) < 1:
            return
            
        operand = self.stack.pop()
        
        # Type checking
        if not isinstance(operand, bool):
            self.errors.append(f"Type error: '!' requires boolean operand")
            return
            
        self.stack.append(not operand)
    
    # Literals
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