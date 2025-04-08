from ExprVisitor import ExprVisitor
from ExprParser import ExprParser

class EvalVisitor(ExprVisitor):
    def __init__(self):
        self.memory = {}  # symbol table (napĹ™. x = 5)

    def visitProg(self, ctx):
        results = []
        for stat in ctx.stat():
            result = self.visit(stat)
            if result is not None:
                results.append(result)
        return results

    def visitStat(self, ctx):
        if ctx.getChildCount() == 1:
            return None  # prĂˇzdnĂ˝ Ĺ™Ăˇdek
        elif ctx.getChild(1).getText() == '=':
            id_name = ctx.ID().getText()
            value = self.visit(ctx.expr())
            self.memory[id_name] = value
            return f"{id_name} = {value}"
        else:
            return self.visit(ctx.expr())

    def visitExpr(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.ID():
            var_name = ctx.ID().getText()
            return self.memory.get(var_name, 0)  # vĂ˝chozĂ­ hodnota 0
        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':  # (expr)
                return self.visit(ctx.expr(0))
            else:  # binĂˇrnĂ­ operace
                left = self.visit(ctx.expr(0))
                right = self.visit(ctx.expr(1))
                op = ctx.getChild(1).getText()
                if op == '+':
                    return left + right
                elif op == '-':
                    return left - right
                elif op == '*':
                    return left * right
                elif op == '/':
                    return left / right
        return None