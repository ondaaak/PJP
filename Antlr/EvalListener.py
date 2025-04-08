from ExprListener import ExprListener
from ExprParser import ExprParser

class EvalListener(ExprListener):
    def __init__(self):
        self.values = {}

    def exitAssign(self, ctx: ExprParser.AssignContext):
        var_name = ctx.ID().getText()
        value = self.evaluate(ctx.expr())  
        self.values[var_name] = value
        print(f"Assigned: {var_name} = {value}")

    def exitExpression(self, ctx: ExprParser.ExpressionContext):
        sub_expr = ctx.expr()
        result = self.evaluate(sub_expr)
        print(f"Expression result: {result}")

    def evaluate(self, ctx):
        if ctx is None:
            return 0

        if isinstance(ctx, ExprParser.AssignContext):
            return self.evaluate(ctx.expr())

        if isinstance(ctx, ExprParser.ParContext):
            return self.evaluate(ctx.expr())

        child_count = ctx.getChildCount()
        if child_count == 3:
            left = ctx.expr(0)
            right = ctx.expr(1)
            op = ctx.getChild(1).getText()
            left_val = self.evaluate(left)
            right_val = self.evaluate(right)
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '*':
                return left_val * right_val
            elif op == '/':
                return left_val / right_val
            elif op == '%':
                return left_val % right_val
            return 0

        if child_count == 1:
            child = ctx.getChild(0)
            token_type = child.getSymbol().type
            parser = ctx.parser
            if token_type == parser.INT:
                return int(child.getText())
            elif token_type == parser.FLOAT:
                return float(child.getText())
            elif token_type == parser.ID:
                return self.values.get(child.getText(), 0)
            elif token_type == parser.STRING:
                return child.getText().strip('"')
            return 0

        return 0