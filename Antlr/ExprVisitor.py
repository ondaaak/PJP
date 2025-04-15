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


    # Visit a parse tree produced by ExprParser#EmptyStatement.
    def visitEmptyStatement(self, ctx:ExprParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ExprStatement.
    def visitExprStatement(self, ctx:ExprParser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Declaration.
    def visitDeclaration(self, ctx:ExprParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#DeclarationWithAssignment.
    def visitDeclarationWithAssignment(self, ctx:ExprParser.DeclarationWithAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ReadStatement.
    def visitReadStatement(self, ctx:ExprParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#WriteStatement.
    def visitWriteStatement(self, ctx:ExprParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#BlockStatement.
    def visitBlockStatement(self, ctx:ExprParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#IfStatement.
    def visitIfStatement(self, ctx:ExprParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#IfElseStatement.
    def visitIfElseStatement(self, ctx:ExprParser.IfElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#WhileStatement.
    def visitWhileStatement(self, ctx:ExprParser.WhileStatementContext):
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


    # Visit a parse tree produced by ExprParser#FloatLiteral.
    def visitFloatLiteral(self, ctx:ExprParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Parens.
    def visitParens(self, ctx:ExprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Relational.
    def visitRelational(self, ctx:ExprParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:ExprParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#LogicalOr.
    def visitLogicalOr(self, ctx:ExprParser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#LogicalNot.
    def visitLogicalNot(self, ctx:ExprParser.LogicalNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Assignment.
    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#AddSubConcat.
    def visitAddSubConcat(self, ctx:ExprParser.AddSubConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#MulDivMod.
    def visitMulDivMod(self, ctx:ExprParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#BoolLiteral.
    def visitBoolLiteral(self, ctx:ExprParser.BoolLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#StringLiteral.
    def visitStringLiteral(self, ctx:ExprParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#LogicalAnd.
    def visitLogicalAnd(self, ctx:ExprParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#IntLiteral.
    def visitIntLiteral(self, ctx:ExprParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Equality.
    def visitEquality(self, ctx:ExprParser.EqualityContext):
        return self.visitChildren(ctx)



del ExprParser