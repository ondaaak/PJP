from ExprVisitor import ExprVisitor

class CodeGenVisitor(ExprVisitor):
    def __init__(self):
        self.code = []
        self.label_counter = -1 
        self.var_types = {}

    def new_label(self):
        self.label_counter += 1
        return self.label_counter

    def visitProg(self, ctx):
        for cmd in ctx.command():
            self.visit(cmd)
        return self.code

    def visitExprStatement(self, ctx):
        self.visit(ctx.expr())
        self.code.append("pop") 

    def visitDeclaration(self, ctx):
        type_ctx = ctx.type_()
        type_name = None
        
        if hasattr(type_ctx, 'INT_TYPE') and type_ctx.INT_TYPE():
            type_name = 'int'
        elif hasattr(type_ctx, 'FLOAT_TYPE') and type_ctx.FLOAT_TYPE():
            type_name = 'float'
        elif hasattr(type_ctx, 'BOOL_TYPE') and type_ctx.BOOL_TYPE():
            type_name = 'bool'
        elif hasattr(type_ctx, 'STRING_TYPE') and type_ctx.STRING_TYPE():
            type_name = 'string'
        elif hasattr(type_ctx, 'FILE_TYPE') and type_ctx.FILE_TYPE():
            type_name = 'FILE'
        else:
            type_text = type_ctx.getText().lower()
            if 'int' in type_text:
                type_name = 'int'
            elif 'float' in type_text:
                type_name = 'float'
            elif 'bool' in type_text:
                type_name = 'bool'
            elif 'string' in type_text:
                type_name = 'string'
            elif 'file' in type_text:
                type_name = 'FILE'
        
        id_list = ctx.ID()
        for id_token in id_list:
            var_name = id_token.getText()
            self.var_types[var_name] = type_name
            
            if type_name == 'int':
                self.code.append("push I 0")
            elif type_name == 'float':
                self.code.append("push F 0.0")
            elif type_name == 'bool':
                self.code.append("push B false")
            elif type_name == 'string':
                self.code.append("push S \"\"")
            elif type_name == 'FILE':
                self.code.append("push S \"\"")
        
            self.code.append(f"save {var_name}")

    def visitDeclarationWithAssignment(self, ctx):
        var_name = ctx.ID().getText()
        type_name = self.visit(ctx.type_())
        self.var_types[var_name] = type_name
        self.visit(ctx.expr())
        self.code.append(f"save {var_name}")

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        var_type = self.var_types.get(var_name) 
        
        expr_ctx = ctx.expr()
        expr_type = self.getExprType(expr_ctx)
        self.visit(expr_ctx)
        
        if var_type == 'float' and expr_type == 'int':
            self.code.append("itof")
        
        self.code.append(f"save {var_name}")
        self.code.append(f"load {var_name}")

    def visitIntLiteral(self, ctx):
        value = ctx.INT().getText()
        self.code.append(f"push I {value}")

    def visitFloatLiteral(self, ctx):
        value = ctx.FLOAT().getText()
        self.code.append(f"push F {value}")

    def visitStringLiteral(self, ctx):
        value = ctx.STRING().getText()
        self.code.append(f"push S {value}")

    def visitBoolLiteral(self, ctx):
        value = ctx.BOOL().getText()
        self.code.append(f"push B {value}")

    def visitVariable(self, ctx):
        var_name = ctx.ID().getText()
        self.code.append(f"load {var_name} ")

    def visitAddSubConcat(self, ctx):
        left_ctx = ctx.expr(0)
        right_ctx = ctx.expr(1)
        left_type = self.getExprType(left_ctx)
        right_type = self.getExprType(right_ctx)
        
        self.visit(left_ctx)
        if left_type == 'int' and right_type == 'float':
            self.code.append("itof")
        self.visit(right_ctx)
        if right_type == 'int' and left_type == 'float':
            self.code.append("itof")
        
        op = ctx.getChild(1).getText()
        if op == '+':
            if left_type == 'float' or right_type == 'float':
                self.code.append("add F")
            else:
                self.code.append("add I")
        elif op == '-':
            if left_type == 'float' or right_type == 'float':
                self.code.append("sub F")
            else:
                self.code.append("sub I")
        elif op == '.':
            self.code.append("concat")

    def visitMulDivMod(self, ctx):
        left_ctx = ctx.expr(0)
        right_ctx = ctx.expr(1)
        left_type = self.getExprType(left_ctx)
        right_type = self.getExprType(right_ctx)
        
        self.visit(left_ctx)
        if left_type == 'int' and right_type == 'float':
            self.code.append("itof")
        self.visit(right_ctx)
        if right_type == 'int' and left_type == 'float':
            self.code.append("itof")
        
        op = ctx.getChild(1).getText()
        if op == '*':
            if left_type == 'float' or right_type == 'float':
                self.code.append("mul F")
            else:
                self.code.append("mul I")
        elif op == '/':
            if left_type == 'float' or right_type == 'float':
                self.code.append("div F")
            else:
                self.code.append("div I")
        elif op == '%':
            self.code.append("mod")
            
    def visitLogicalAnd(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.code.append("and")

    def visitLogicalOr(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.code.append("or")

    def visitLogicalNot(self, ctx):
        self.visit(ctx.expr())
        self.code.append("not")

    def visitRelational(self, ctx):
        left_ctx = ctx.expr(0)
        right_ctx = ctx.expr(1)
        left_type = self.getExprType(left_ctx)
        right_type = self.getExprType(right_ctx)

        self.visit(left_ctx)
        if left_type == 'int' and right_type == 'float':
            self.code.append("itof")
        self.visit(right_ctx)
        if right_type == 'int' and left_type == 'float':
            self.code.append("itof")

        op = ctx.getChild(1).getText()
        if op == '<':
            if left_type == 'float' or right_type == 'float':
                self.code.append("lt F")
            else:
                self.code.append("lt I")
        elif op == '>':
            if left_type == 'float' or right_type == 'float':
                self.code.append("gt F")
            else:
                self.code.append("gt I")

    def visitEquality(self, ctx):
        left_ctx = ctx.expr(0)
        right_ctx = ctx.expr(1)
        
        left_type = self.getExprType(left_ctx)
        right_type = self.getExprType(right_ctx)
        
        self.visit(left_ctx)
        self.visit(right_ctx)
        
        op = ctx.getChild(1).getText() 
        
        eq_type = "I"  
        if left_type == 'string' or right_type == 'string':
            eq_type = "S"
        elif left_type == 'float' or right_type == 'float':
            eq_type = "F"
        
        self.code.append(f"eq {eq_type}")
        
        if op == '!=':
            self.code.append("not")

    def visitUnaryMinus(self, ctx):
        self.visit(ctx.expr())
        self.code.append("uminus I") 

    def visitItf(self, ctx):
        self.visit(ctx.expr())
        self.code.append("itof")

    def visitWriteStatement(self, ctx):
        n = len(ctx.expr())
        for expr_ctx in ctx.expr():
            self.visit(expr_ctx)
        self.code.append(f"print {n}")

    def getExprType(self, ctx):
        if hasattr(ctx, 'INT'):
            return 'int'
        if hasattr(ctx, 'FLOAT'):
            return 'float'
        if hasattr(ctx, 'STRING'):
            return 'string'
        if hasattr(ctx, 'BOOL'):
            return 'bool'
        if hasattr(ctx, 'ID'):
            var_name = ctx.ID().getText()
            return self.var_types.get(var_name, None)
        return None

    def visitWhileStatement(self, ctx):
        start_label = self.new_label()
        end_label = self.new_label()
        
        self.code.append(f"label {start_label}")
        
        self.visit(ctx.expr())
        
        self.code.append(f"fjmp {end_label}")
        
        self.visit(ctx.statement())
        
        self.code.append(f"jmp {start_label}")
        
        self.code.append(f"label {end_label}")

    def visitIfStatement(self, ctx):
        end_label = self.new_label()
        
        self.visit(ctx.expr())
        
        self.code.append(f"fjmp {end_label}")
        
        self.visit(ctx.statement())
        
        next_label = self.new_label()
        self.code.append(f"jmp {next_label}")
        
        self.code.append(f"label {end_label}")
        
        self.code.append(f"label {next_label}")

    def visitIfElseStatement(self, ctx):
        else_label = self.new_label()
        end_label = self.new_label()
        
        self.visit(ctx.expr())
        
        self.code.append(f"fjmp {else_label}")
        
        self.visit(ctx.statement(0))
        
        self.code.append(f"jmp {end_label}")
        
        self.code.append(f"label {else_label}")
        
        self.visit(ctx.statement(1))
        
        self.code.append(f"label {end_label}")

    def visitReadStatement(self, ctx):
        for id_ctx in ctx.ID():
            var_name = id_ctx.getText()
            typ = self.var_types.get(var_name, None)
            if typ == 'int':
                self.code.append("read I")
            elif typ == 'float':
                self.code.append("read F")
            elif typ == 'string':
                self.code.append("read S")
            elif typ == 'bool':
                self.code.append("read B")
            else:
                self.code.append("read I")
            self.code.append(f"save {var_name}")

    def visitType(self, ctx):
        if ctx.INT_TYPE():
            return 'int'
        elif ctx.FLOAT_TYPE():
            return 'float'
        elif ctx.BOOL_TYPE():
            return 'bool'
        elif ctx.STRING_TYPE():
            return 'string'
        elif ctx.FILE_TYPE():
            return 'FILE'
        return self.visitChildren(ctx)