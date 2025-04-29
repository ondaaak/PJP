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


    # Enter a parse tree produced by ExprParser#FileType.
    def enterFileType(self, ctx:ExprParser.FileTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#FileType.
    def exitFileType(self, ctx:ExprParser.FileTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#ShiftRight.
    def enterShiftRight(self, ctx:ExprParser.ShiftRightContext):
        pass

    # Exit a parse tree produced by ExprParser#ShiftRight.
    def exitShiftRight(self, ctx:ExprParser.ShiftRightContext):
        pass


    # Enter a parse tree produced by ExprParser#Variable.
    def enterVariable(self, ctx:ExprParser.VariableContext):
        pass

    # Exit a parse tree produced by ExprParser#Variable.
    def exitVariable(self, ctx:ExprParser.VariableContext):
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


    # Enter a parse tree produced by ExprParser#Relational.
    def enterRelational(self, ctx:ExprParser.RelationalContext):
        pass

    # Exit a parse tree produced by ExprParser#Relational.
    def exitRelational(self, ctx:ExprParser.RelationalContext):
        pass


    # Enter a parse tree produced by ExprParser#UnaryMinus.
    def enterUnaryMinus(self, ctx:ExprParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by ExprParser#UnaryMinus.
    def exitUnaryMinus(self, ctx:ExprParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by ExprParser#LogicalOr.
    def enterLogicalOr(self, ctx:ExprParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by ExprParser#LogicalOr.
    def exitLogicalOr(self, ctx:ExprParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by ExprParser#LogicalNot.
    def enterLogicalNot(self, ctx:ExprParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by ExprParser#LogicalNot.
    def exitLogicalNot(self, ctx:ExprParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by ExprParser#Assignment.
    def enterAssignment(self, ctx:ExprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#Assignment.
    def exitAssignment(self, ctx:ExprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#MulDivMod.
    def enterMulDivMod(self, ctx:ExprParser.MulDivModContext):
        pass

    # Exit a parse tree produced by ExprParser#MulDivMod.
    def exitMulDivMod(self, ctx:ExprParser.MulDivModContext):
        pass


    # Enter a parse tree produced by ExprParser#AddSubConcat.
    def enterAddSubConcat(self, ctx:ExprParser.AddSubConcatContext):
        pass

    # Exit a parse tree produced by ExprParser#AddSubConcat.
    def exitAddSubConcat(self, ctx:ExprParser.AddSubConcatContext):
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


    # Enter a parse tree produced by ExprParser#LogicalAnd.
    def enterLogicalAnd(self, ctx:ExprParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by ExprParser#LogicalAnd.
    def exitLogicalAnd(self, ctx:ExprParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by ExprParser#IntLiteral.
    def enterIntLiteral(self, ctx:ExprParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by ExprParser#IntLiteral.
    def exitIntLiteral(self, ctx:ExprParser.IntLiteralContext):
        pass


    # Enter a parse tree produced by ExprParser#Equality.
    def enterEquality(self, ctx:ExprParser.EqualityContext):
        pass

    # Exit a parse tree produced by ExprParser#Equality.
    def exitEquality(self, ctx:ExprParser.EqualityContext):
        pass



del ExprParser