# Generated from Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,70,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,39,8,2,1,3,1,3,1,3,1,
        3,3,3,45,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,57,8,4,
        1,4,1,4,1,4,1,4,1,4,1,4,5,4,65,8,4,10,4,12,4,68,9,4,1,4,0,1,8,5,
        0,2,4,6,8,0,2,1,0,3,4,1,0,5,6,78,0,13,1,0,0,0,2,18,1,0,0,0,4,38,
        1,0,0,0,6,44,1,0,0,0,8,56,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,
        15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,
        0,16,17,5,0,0,1,17,1,1,0,0,0,18,19,3,4,2,0,19,3,1,0,0,0,20,21,3,
        8,4,0,21,22,5,1,0,0,22,39,1,0,0,0,23,24,5,14,0,0,24,25,5,2,0,0,25,
        26,3,8,4,0,26,27,5,1,0,0,27,39,1,0,0,0,28,29,3,6,3,0,29,30,5,14,
        0,0,30,31,5,1,0,0,31,39,1,0,0,0,32,33,3,6,3,0,33,34,5,14,0,0,34,
        35,5,2,0,0,35,36,3,8,4,0,36,37,5,1,0,0,37,39,1,0,0,0,38,20,1,0,0,
        0,38,23,1,0,0,0,38,28,1,0,0,0,38,32,1,0,0,0,39,5,1,0,0,0,40,45,5,
        9,0,0,41,45,5,10,0,0,42,45,5,11,0,0,43,45,5,12,0,0,44,40,1,0,0,0,
        44,41,1,0,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,7,1,0,0,0,46,47,6,4,
        -1,0,47,57,5,15,0,0,48,57,5,16,0,0,49,57,5,13,0,0,50,57,5,17,0,0,
        51,57,5,14,0,0,52,53,5,7,0,0,53,54,3,8,4,0,54,55,5,8,0,0,55,57,1,
        0,0,0,56,46,1,0,0,0,56,48,1,0,0,0,56,49,1,0,0,0,56,50,1,0,0,0,56,
        51,1,0,0,0,56,52,1,0,0,0,57,66,1,0,0,0,58,59,10,8,0,0,59,60,7,0,
        0,0,60,65,3,8,4,9,61,62,10,7,0,0,62,63,7,1,0,0,63,65,3,8,4,8,64,
        58,1,0,0,0,64,61,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,
        0,67,9,1,0,0,0,68,66,1,0,0,0,6,13,38,44,56,64,66
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'*'", "'/'", "'+'", "'-'", 
                     "'('", "')'", "'int'", "'float'", "'bool'", "'string'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", 
                      "STRING_TYPE", "BOOL", "ID", "INT", "FLOAT", "STRING", 
                      "WS", "COMMENT" ]

    RULE_prog = 0
    RULE_command = 1
    RULE_statement = 2
    RULE_type = 3
    RULE_expr = 4

    ruleNames =  [ "prog", "command", "statement", "type", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    INT_TYPE=9
    FLOAT_TYPE=10
    BOOL_TYPE=11
    STRING_TYPE=12
    BOOL=13
    ID=14
    INT=15
    FLOAT=16
    STRING=17
    WS=18
    COMMENT=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.CommandContext)
            else:
                return self.getTypedRuleContext(ExprParser.CommandContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 261760) != 0):
                self.state = 10
                self.command()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = ExprParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignmentContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationWithAssignmentContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(ExprParser.TypeContext,0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationWithAssignment" ):
                listener.enterDeclarationWithAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationWithAssignment" ):
                listener.exitDeclarationWithAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationWithAssignment" ):
                return visitor.visitDeclarationWithAssignment(self)
            else:
                return visitor.visitChildren(self)


    class ExprStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStatement" ):
                listener.enterExprStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStatement" ):
                listener.exitExprStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStatement" ):
                return visitor.visitExprStatement(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(ExprParser.TypeContext,0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = ExprParser.ExprStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.expr(0)
                self.state = 21
                self.match(ExprParser.T__0)
                pass

            elif la_ == 2:
                localctx = ExprParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(ExprParser.ID)
                self.state = 24
                self.match(ExprParser.T__1)
                self.state = 25
                self.expr(0)
                self.state = 26
                self.match(ExprParser.T__0)
                pass

            elif la_ == 3:
                localctx = ExprParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.type_()
                self.state = 29
                self.match(ExprParser.ID)
                self.state = 30
                self.match(ExprParser.T__0)
                pass

            elif la_ == 4:
                localctx = ExprParser.DeclarationWithAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.type_()
                self.state = 33
                self.match(ExprParser.ID)
                self.state = 34
                self.match(ExprParser.T__1)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(ExprParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BoolTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_TYPE(self):
            return self.getToken(ExprParser.BOOL_TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolType" ):
                listener.enterBoolType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolType" ):
                listener.exitBoolType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolType" ):
                return visitor.visitBoolType(self)
            else:
                return visitor.visitChildren(self)


    class StringTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_TYPE(self):
            return self.getToken(ExprParser.STRING_TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringType" ):
                listener.enterStringType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringType" ):
                listener.exitStringType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringType" ):
                return visitor.visitStringType(self)
            else:
                return visitor.visitChildren(self)


    class IntTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_TYPE(self):
            return self.getToken(ExprParser.INT_TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntType" ):
                listener.enterIntType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntType" ):
                listener.exitIntType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntType" ):
                return visitor.visitIntType(self)
            else:
                return visitor.visitChildren(self)


    class FloatTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_TYPE(self):
            return self.getToken(ExprParser.FLOAT_TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatType" ):
                listener.enterFloatType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatType" ):
                listener.exitFloatType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatType" ):
                return visitor.visitFloatType(self)
            else:
                return visitor.visitChildren(self)



    def type_(self):

        localctx = ExprParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = ExprParser.IntTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(ExprParser.INT_TYPE)
                pass
            elif token in [10]:
                localctx = ExprParser.FloatTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(ExprParser.FLOAT_TYPE)
                pass
            elif token in [11]:
                localctx = ExprParser.BoolTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.match(ExprParser.BOOL_TYPE)
                pass
            elif token in [12]:
                localctx = ExprParser.StringTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.match(ExprParser.STRING_TYPE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class BoolLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(ExprParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolLiteral" ):
                listener.enterBoolLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolLiteral" ):
                listener.exitBoolLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolLiteral" ):
                return visitor.visitBoolLiteral(self)
            else:
                return visitor.visitChildren(self)


    class StringLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class FloatLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatLiteral" ):
                listener.enterFloatLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatLiteral" ):
                listener.exitFloatLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLiteral" ):
                return visitor.visitFloatLiteral(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class IntLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLiteral" ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLiteral" ):
                listener.exitIntLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLiteral" ):
                return visitor.visitIntLiteral(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = ExprParser.IntLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 47
                self.match(ExprParser.INT)
                pass
            elif token in [16]:
                localctx = ExprParser.FloatLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(ExprParser.FLOAT)
                pass
            elif token in [13]:
                localctx = ExprParser.BoolLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.match(ExprParser.BOOL)
                pass
            elif token in [17]:
                localctx = ExprParser.StringLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 50
                self.match(ExprParser.STRING)
                pass
            elif token in [14]:
                localctx = ExprParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                self.match(ExprParser.ID)
                pass
            elif token in [7]:
                localctx = ExprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(ExprParser.T__6)
                self.state = 53
                self.expr(0)
                self.state = 54
                self.match(ExprParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 64
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.MulDivContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 59
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.AddSubContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 62
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 63
                        self.expr(8)
                        pass

             
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         




