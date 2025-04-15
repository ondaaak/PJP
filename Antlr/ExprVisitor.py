# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#command.
    def visitCommand(self, ctx:ExprParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ExprStatement.
    def visitExprStatement(self, ctx:ExprParser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Assignment.
    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Declaration.
    def visitDeclaration(self, ctx:ExprParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#DeclarationWithAssignment.
    def visitDeclarationWithAssignment(self, ctx:ExprParser.DeclarationWithAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#IntType.
    def visitIntType(self, ctx:ExprParser.IntTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#FloatType.
    def visitFloatType(self, ctx:ExprParser.FloatTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#BoolType.
    def visitBoolType(self, ctx:ExprParser.BoolTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#StringType.
    def visitStringType(self, ctx:ExprParser.StringTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Variable.
    def visitVariable(self, ctx:ExprParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#BoolLiteral.
    def visitBoolLiteral(self, ctx:ExprParser.BoolLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#StringLiteral.
    def visitStringLiteral(self, ctx:ExprParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#MulDiv.
    def visitMulDiv(self, ctx:ExprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#AddSub.
    def visitAddSub(self, ctx:ExprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#FloatLiteral.
    def visitFloatLiteral(self, ctx:ExprParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Parens.
    def visitParens(self, ctx:ExprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#IntLiteral.
    def visitIntLiteral(self, ctx:ExprParser.IntLiteralContext):
        return self.visitChildren(ctx)



del ExprParser