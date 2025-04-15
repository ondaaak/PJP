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


    # Enter a parse tree produced by ExprParser#EmptyStatement.
    def enterEmptyStatement(self, ctx:ExprParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#EmptyStatement.
    def exitEmptyStatement(self, ctx:ExprParser.EmptyStatementContext):
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


    # Enter a parse tree produced by ExprParser#Declaration.
    def enterDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#Declaration.
    def exitDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#DeclarationWithAssignment.
    def enterDeclarationWithAssignment(self, ctx:ExprParser.DeclarationWithAssignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#DeclarationWithAssignment.
    def exitDeclarationWithAssignment(self, ctx:ExprParser.DeclarationWithAssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#ReadStatement.
    def enterReadStatement(self, ctx:ExprParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#ReadStatement.
    def exitReadStatement(self, ctx:ExprParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#WriteStatement.
    def enterWriteStatement(self, ctx:ExprParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#WriteStatement.
    def exitWriteStatement(self, ctx:ExprParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#BlockStatement.
    def enterBlockStatement(self, ctx:ExprParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#BlockStatement.
    def exitBlockStatement(self, ctx:ExprParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#IfStatement.
    def enterIfStatement(self, ctx:ExprParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#IfStatement.
    def exitIfStatement(self, ctx:ExprParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#IfElseStatement.
    def enterIfElseStatement(self, ctx:ExprParser.IfElseStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#IfElseStatement.
    def exitIfElseStatement(self, ctx:ExprParser.IfElseStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#WhileStatement.
    def enterWhileStatement(self, ctx:ExprParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#WhileStatement.
    def exitWhileStatement(self, ctx:ExprParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#IntType.
    def enterIntType(self, ctx:ExprParser.IntTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#IntType.
    def exitIntType(self, ctx:ExprParser.IntTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#FloatType.
    def enterFloatType(self, ctx:ExprParser.FloatTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#FloatType.
    def exitFloatType(self, ctx:ExprParser.FloatTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#BoolType.
    def enterBoolType(self, ctx:ExprParser.BoolTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#BoolType.
    def exitBoolType(self, ctx:ExprParser.BoolTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#StringType.
    def enterStringType(self, ctx:ExprParser.StringTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#StringType.
    def exitStringType(self, ctx:ExprParser.StringTypeContext):
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


    # Enter a parse tree produced by ExprParser#Comparison.
    def enterComparison(self, ctx:ExprParser.ComparisonContext):
        pass

    # Exit a parse tree produced by ExprParser#Comparison.
    def exitComparison(self, ctx:ExprParser.ComparisonContext):
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


    # Enter a parse tree produced by ExprParser#LogicalOp.
    def enterLogicalOp(self, ctx:ExprParser.LogicalOpContext):
        pass

    # Exit a parse tree produced by ExprParser#LogicalOp.
    def exitLogicalOp(self, ctx:ExprParser.LogicalOpContext):
        pass


    # Enter a parse tree produced by ExprParser#IntLiteral.
    def enterIntLiteral(self, ctx:ExprParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by ExprParser#IntLiteral.
    def exitIntLiteral(self, ctx:ExprParser.IntLiteralContext):
        pass


    # Enter a parse tree produced by ExprParser#NotOp.
    def enterNotOp(self, ctx:ExprParser.NotOpContext):
        pass

    # Exit a parse tree produced by ExprParser#NotOp.
    def exitNotOp(self, ctx:ExprParser.NotOpContext):
        pass



del ExprParser