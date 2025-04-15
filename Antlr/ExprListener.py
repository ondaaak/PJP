# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#command.
    def enterCommand(self, ctx:ExprParser.CommandContext):
        pass

    # Exit a parse tree produced by ExprParser#command.
    def exitCommand(self, ctx:ExprParser.CommandContext):
        pass


    # Enter a parse tree produced by ExprParser#ExprStatement.
    def enterExprStatement(self, ctx:ExprParser.ExprStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#ExprStatement.
    def exitExprStatement(self, ctx:ExprParser.ExprStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#Assignment.
    def enterAssignment(self, ctx:ExprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#Assignment.
    def exitAssignment(self, ctx:ExprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#Variable.
    def enterVariable(self, ctx:ExprParser.VariableContext):
        pass

    # Exit a parse tree produced by ExprParser#Variable.
    def exitVariable(self, ctx:ExprParser.VariableContext):
        pass


    # Enter a parse tree produced by ExprParser#BoolLiteral.
    def enterBoolLiteral(self, ctx:ExprParser.BoolLiteralContext):
        pass

    # Exit a parse tree produced by ExprParser#BoolLiteral.
    def exitBoolLiteral(self, ctx:ExprParser.BoolLiteralContext):
        pass


    # Enter a parse tree produced by ExprParser#StringLiteral.
    def enterStringLiteral(self, ctx:ExprParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by ExprParser#StringLiteral.
    def exitStringLiteral(self, ctx:ExprParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by ExprParser#MulDiv.
    def enterMulDiv(self, ctx:ExprParser.MulDivContext):
        pass

    # Exit a parse tree produced by ExprParser#MulDiv.
    def exitMulDiv(self, ctx:ExprParser.MulDivContext):
        pass


    # Enter a parse tree produced by ExprParser#AddSub.
    def enterAddSub(self, ctx:ExprParser.AddSubContext):
        pass

    # Exit a parse tree produced by ExprParser#AddSub.
    def exitAddSub(self, ctx:ExprParser.AddSubContext):
        pass


    # Enter a parse tree produced by ExprParser#FloatLiteral.
    def enterFloatLiteral(self, ctx:ExprParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by ExprParser#FloatLiteral.
    def exitFloatLiteral(self, ctx:ExprParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by ExprParser#Parens.
    def enterParens(self, ctx:ExprParser.ParensContext):
        pass

    # Exit a parse tree produced by ExprParser#Parens.
    def exitParens(self, ctx:ExprParser.ParensContext):
        pass


    # Enter a parse tree produced by ExprParser#IntLiteral.
    def enterIntLiteral(self, ctx:ExprParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by ExprParser#IntLiteral.
    def exitIntLiteral(self, ctx:ExprParser.IntLiteralContext):
        pass



del ExprParser