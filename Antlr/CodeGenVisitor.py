from ExprVisitor import ExprVisitor

class CodeGenVisitor(ExprVisitor):
    def __init__(self):
        self.code = []
    
    def visitProg(self, ctx):
        for cmd in ctx.command():
            self.visit(cmd)
        return self.code

    def visitExprStatement(self, ctx):
        self.visit(ctx.expr())
        self.code.append("pop")  # zahodí výsledek výrazu

    def visitDeclarationWithAssignment(self, ctx):
        var_name = ctx.ID().getText()
        self.visit(ctx.expr())
        self.code.append(f"save {var_name}")

    def visitDeclaration(self, ctx):
        # pouze deklarace bez přiřazení, není potřeba generovat kód
        pass

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        self.visit(ctx.expr())
        self.code.append(f"save {var_name}")

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
        self.code.append(f"load {var_name}")

    def visitAddSubConcat(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '+':
            # Zjisti typ (I nebo F) podle typu operandů, zde zjednodušeně I
            self.code.append("add I")
        elif op == '-':
            self.code.append("sub I")
        elif op == '.':
            self.code.append("concat")
    
    def visitMulDivMod(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '*':
            self.code.append("mul I")  # nebo "mul F" podle typu
        elif op == '/':
            self.code.append("div I")  # nebo "div F" podle typu
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
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '>':
            self.code.append("gt I")  # nebo "gt F" podle typu
        elif op == '<':
            self.code.append("lt I")  # nebo "lt F" podle typu
        elif op == '>=':
            # gt + eq kombinace, nebo přidej instrukci dle zadání
            pass
        elif op == '<=':
            # lt + eq kombinace, nebo přidej instrukci dle zadání
            pass

    def visitEquality(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.code.append("eq I")  # nebo "eq F" nebo "eq S" podle typu

    def visitUnaryMinus(self, ctx):
        self.visit(ctx.expr())
        self.code.append("uminus I")  # nebo "uminus F" podle typu

    def visitItf(self, ctx):
        self.visit(ctx.expr())
        self.code.append("itof")