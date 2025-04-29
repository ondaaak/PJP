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
        4,1,40,145,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,
        0,10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,5,2,29,8,2,10,2,12,2,32,9,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,5,2,46,8,2,10,2,12,2,49,9,2,1,2,1,2,1,2,1,2,1,2,5,
        2,56,8,2,10,2,12,2,59,9,2,1,2,1,2,1,2,1,2,5,2,65,8,2,10,2,12,2,68,
        9,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,91,8,2,1,3,1,3,1,3,1,3,1,3,3,3,98,8,
        3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,117,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,140,8,4,10,4,12,4,143,
        9,4,1,4,0,1,8,5,0,2,4,6,8,0,4,1,0,27,28,1,0,29,32,1,0,8,10,2,0,11,
        12,33,33,172,0,13,1,0,0,0,2,18,1,0,0,0,4,90,1,0,0,0,6,97,1,0,0,0,
        8,116,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,
        0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,17,
        1,1,0,0,0,18,19,3,4,2,0,19,3,1,0,0,0,20,91,5,1,0,0,21,22,3,8,4,0,
        22,23,5,1,0,0,23,91,1,0,0,0,24,25,3,6,3,0,25,30,5,35,0,0,26,27,5,
        2,0,0,27,29,5,35,0,0,28,26,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,
        31,1,0,0,0,31,33,1,0,0,0,32,30,1,0,0,0,33,34,5,1,0,0,34,91,1,0,0,
        0,35,36,3,6,3,0,36,37,5,35,0,0,37,38,5,3,0,0,38,39,3,8,4,0,39,40,
        5,1,0,0,40,91,1,0,0,0,41,42,5,16,0,0,42,47,5,35,0,0,43,44,5,2,0,
        0,44,46,5,35,0,0,45,43,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,
        1,0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,50,91,5,1,0,0,51,52,5,17,0,0,
        52,57,3,8,4,0,53,54,5,2,0,0,54,56,3,8,4,0,55,53,1,0,0,0,56,59,1,
        0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,
        61,5,1,0,0,61,91,1,0,0,0,62,66,5,4,0,0,63,65,3,4,2,0,64,63,1,0,0,
        0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,66,
        1,0,0,0,69,91,5,5,0,0,70,71,5,13,0,0,71,72,5,6,0,0,72,73,3,8,4,0,
        73,74,5,7,0,0,74,75,3,4,2,0,75,91,1,0,0,0,76,77,5,13,0,0,77,78,5,
        6,0,0,78,79,3,8,4,0,79,80,5,7,0,0,80,81,3,4,2,0,81,82,5,14,0,0,82,
        83,3,4,2,0,83,91,1,0,0,0,84,85,5,15,0,0,85,86,5,6,0,0,86,87,3,8,
        4,0,87,88,5,7,0,0,88,89,3,4,2,0,89,91,1,0,0,0,90,20,1,0,0,0,90,21,
        1,0,0,0,90,24,1,0,0,0,90,35,1,0,0,0,90,41,1,0,0,0,90,51,1,0,0,0,
        90,62,1,0,0,0,90,70,1,0,0,0,90,76,1,0,0,0,90,84,1,0,0,0,91,5,1,0,
        0,0,92,98,5,18,0,0,93,98,5,19,0,0,94,98,5,20,0,0,95,98,5,21,0,0,
        96,98,5,22,0,0,97,92,1,0,0,0,97,93,1,0,0,0,97,94,1,0,0,0,97,95,1,
        0,0,0,97,96,1,0,0,0,98,7,1,0,0,0,99,100,6,4,-1,0,100,101,5,26,0,
        0,101,117,3,8,4,9,102,103,5,12,0,0,103,117,3,8,4,8,104,105,5,35,
        0,0,105,106,5,3,0,0,106,117,3,8,4,7,107,117,5,36,0,0,108,117,5,37,
        0,0,109,117,5,34,0,0,110,117,5,38,0,0,111,117,5,35,0,0,112,113,5,
        6,0,0,113,114,3,8,4,0,114,115,5,7,0,0,115,117,1,0,0,0,116,99,1,0,
        0,0,116,102,1,0,0,0,116,104,1,0,0,0,116,107,1,0,0,0,116,108,1,0,
        0,0,116,109,1,0,0,0,116,110,1,0,0,0,116,111,1,0,0,0,116,112,1,0,
        0,0,117,141,1,0,0,0,118,119,10,16,0,0,119,120,5,24,0,0,120,140,3,
        8,4,17,121,122,10,15,0,0,122,123,5,25,0,0,123,140,3,8,4,16,124,125,
        10,14,0,0,125,126,7,0,0,0,126,140,3,8,4,15,127,128,10,13,0,0,128,
        129,7,1,0,0,129,140,3,8,4,14,130,131,10,12,0,0,131,132,7,2,0,0,132,
        140,3,8,4,13,133,134,10,11,0,0,134,135,5,23,0,0,135,140,3,8,4,12,
        136,137,10,10,0,0,137,138,7,3,0,0,138,140,3,8,4,11,139,118,1,0,0,
        0,139,121,1,0,0,0,139,124,1,0,0,0,139,127,1,0,0,0,139,130,1,0,0,
        0,139,133,1,0,0,0,139,136,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,
        0,141,142,1,0,0,0,142,9,1,0,0,0,143,141,1,0,0,0,10,13,30,47,57,66,
        90,97,116,139,141
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'='", "'{'", "'}'", "'('", 
                     "')'", "'*'", "'/'", "'%'", "'+'", "'-'", "'if'", "'else'", 
                     "'while'", "'read'", "'write'", "'int'", "'float'", 
                     "'bool'", "'string'", "'FILE'", "'>>'", "'&&'", "'||'", 
                     "'!'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IF", "ELSE", "WHILE", "READ", "WRITE", 
                      "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", "STRING_TYPE", 
                      "FILE_TYPE", "SHR", "AND", "OR", "NOT", "EQ", "NEQ", 
                      "LT", "GT", "LE", "GE", "CONCAT", "BOOL", "ID", "INT", 
                      "FLOAT", "STRING", "WS", "COMMENT" ]

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
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    IF=13
    ELSE=14
    WHILE=15
    READ=16
    WRITE=17
    INT_TYPE=18
    FLOAT_TYPE=19
    BOOL_TYPE=20
    STRING_TYPE=21
    FILE_TYPE=22
    SHR=23
    AND=24
    OR=25
    NOT=26
    EQ=27
    NEQ=28
    LT=29
    GT=30
    LE=31
    GE=32
    CONCAT=33
    BOOL=34
    ID=35
    INT=36
    FLOAT=37
    STRING=38
    WS=39
    COMMENT=40

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 532651421778) != 0):
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



    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(ExprParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
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


    class ReadStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(ExprParser.READ, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStatement" ):
                listener.enterReadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStatement" ):
                listener.exitReadStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStatement" ):
                return visitor.visitReadStatement(self)
            else:
                return visitor.visitChildren(self)


    class EmptyStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStatement" ):
                return visitor.visitEmptyStatement(self)
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


    class IfElseStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(ExprParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)

        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElseStatement" ):
                listener.enterIfElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElseStatement" ):
                listener.exitIfElseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseStatement" ):
                return visitor.visitIfElseStatement(self)
            else:
                return visitor.visitChildren(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(ExprParser.WRITE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStatement" ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStatement" ):
                listener.exitWriteStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStatement" ):
                return visitor.visitWriteStatement(self)
            else:
                return visitor.visitChildren(self)


    class BlockStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(ExprParser.TypeContext,0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

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


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = ExprParser.EmptyStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(ExprParser.T__0)
                pass

            elif la_ == 2:
                localctx = ExprParser.ExprStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.expr(0)
                self.state = 22
                self.match(ExprParser.T__0)
                pass

            elif la_ == 3:
                localctx = ExprParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.type_()
                self.state = 25
                self.match(ExprParser.ID)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 26
                    self.match(ExprParser.T__1)
                    self.state = 27
                    self.match(ExprParser.ID)
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 33
                self.match(ExprParser.T__0)
                pass

            elif la_ == 4:
                localctx = ExprParser.DeclarationWithAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.type_()
                self.state = 36
                self.match(ExprParser.ID)
                self.state = 37
                self.match(ExprParser.T__2)
                self.state = 38
                self.expr(0)
                self.state = 39
                self.match(ExprParser.T__0)
                pass

            elif la_ == 5:
                localctx = ExprParser.ReadStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 41
                self.match(ExprParser.READ)
                self.state = 42
                self.match(ExprParser.ID)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 43
                    self.match(ExprParser.T__1)
                    self.state = 44
                    self.match(ExprParser.ID)
                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 50
                self.match(ExprParser.T__0)
                pass

            elif la_ == 6:
                localctx = ExprParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.match(ExprParser.WRITE)
                self.state = 52
                self.expr(0)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 53
                    self.match(ExprParser.T__1)
                    self.state = 54
                    self.expr(0)
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 60
                self.match(ExprParser.T__0)
                pass

            elif la_ == 7:
                localctx = ExprParser.BlockStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 62
                self.match(ExprParser.T__3)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 532651421778) != 0):
                    self.state = 63
                    self.statement()
                    self.state = 68
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 69
                self.match(ExprParser.T__4)
                pass

            elif la_ == 8:
                localctx = ExprParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 70
                self.match(ExprParser.IF)
                self.state = 71
                self.match(ExprParser.T__5)
                self.state = 72
                self.expr(0)
                self.state = 73
                self.match(ExprParser.T__6)
                self.state = 74
                self.statement()
                pass

            elif la_ == 9:
                localctx = ExprParser.IfElseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 76
                self.match(ExprParser.IF)
                self.state = 77
                self.match(ExprParser.T__5)
                self.state = 78
                self.expr(0)
                self.state = 79
                self.match(ExprParser.T__6)
                self.state = 80
                self.statement()
                self.state = 81
                self.match(ExprParser.ELSE)
                self.state = 82
                self.statement()
                pass

            elif la_ == 10:
                localctx = ExprParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 84
                self.match(ExprParser.WHILE)
                self.state = 85
                self.match(ExprParser.T__5)
                self.state = 86
                self.expr(0)
                self.state = 87
                self.match(ExprParser.T__6)
                self.state = 88
                self.statement()
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


    class FileTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FILE_TYPE(self):
            return self.getToken(ExprParser.FILE_TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFileType" ):
                listener.enterFileType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFileType" ):
                listener.exitFileType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFileType" ):
                return visitor.visitFileType(self)
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
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = ExprParser.IntTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(ExprParser.INT_TYPE)
                pass
            elif token in [19]:
                localctx = ExprParser.FloatTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(ExprParser.FLOAT_TYPE)
                pass
            elif token in [20]:
                localctx = ExprParser.BoolTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.match(ExprParser.BOOL_TYPE)
                pass
            elif token in [21]:
                localctx = ExprParser.StringTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 95
                self.match(ExprParser.STRING_TYPE)
                pass
            elif token in [22]:
                localctx = ExprParser.FileTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 96
                self.match(ExprParser.FILE_TYPE)
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


    class ShiftRightContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def SHR(self):
            return self.getToken(ExprParser.SHR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShiftRight" ):
                listener.enterShiftRight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShiftRight" ):
                listener.exitShiftRight(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShiftRight" ):
                return visitor.visitShiftRight(self)
            else:
                return visitor.visitChildren(self)


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


    class RelationalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def LT(self):
            return self.getToken(ExprParser.LT, 0)
        def GT(self):
            return self.getToken(ExprParser.GT, 0)
        def LE(self):
            return self.getToken(ExprParser.LE, 0)
        def GE(self):
            return self.getToken(ExprParser.GE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational" ):
                listener.enterRelational(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational" ):
                listener.exitRelational(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class LogicalOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def OR(self):
            return self.getToken(ExprParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOr" ):
                listener.enterLogicalOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOr" ):
                listener.exitLogicalOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOr" ):
                return visitor.visitLogicalOr(self)
            else:
                return visitor.visitChildren(self)


    class LogicalNotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalNot" ):
                listener.enterLogicalNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalNot" ):
                listener.exitLogicalNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalNot" ):
                return visitor.visitLogicalNot(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
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


    class MulDivModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivMod" ):
                listener.enterMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivMod" ):
                listener.exitMulDivMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivMod" ):
                return visitor.visitMulDivMod(self)
            else:
                return visitor.visitChildren(self)


    class AddSubConcatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def CONCAT(self):
            return self.getToken(ExprParser.CONCAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubConcat" ):
                listener.enterAddSubConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubConcat" ):
                listener.exitAddSubConcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubConcat" ):
                return visitor.visitAddSubConcat(self)
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


    class LogicalAndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def AND(self):
            return self.getToken(ExprParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAnd" ):
                listener.enterLogicalAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAnd" ):
                listener.exitLogicalAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAnd" ):
                return visitor.visitLogicalAnd(self)
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


    class EqualityContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)
        def NEQ(self):
            return self.getToken(ExprParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
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
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = ExprParser.LogicalNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 100
                self.match(ExprParser.NOT)
                self.state = 101
                self.expr(9)
                pass

            elif la_ == 2:
                localctx = ExprParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 102
                self.match(ExprParser.T__11)
                self.state = 103
                self.expr(8)
                pass

            elif la_ == 3:
                localctx = ExprParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 104
                self.match(ExprParser.ID)
                self.state = 105
                self.match(ExprParser.T__2)
                self.state = 106
                self.expr(7)
                pass

            elif la_ == 4:
                localctx = ExprParser.IntLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(ExprParser.INT)
                pass

            elif la_ == 5:
                localctx = ExprParser.FloatLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(ExprParser.FLOAT)
                pass

            elif la_ == 6:
                localctx = ExprParser.BoolLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                self.match(ExprParser.BOOL)
                pass

            elif la_ == 7:
                localctx = ExprParser.StringLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.match(ExprParser.STRING)
                pass

            elif la_ == 8:
                localctx = ExprParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.match(ExprParser.ID)
                pass

            elif la_ == 9:
                localctx = ExprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 112
                self.match(ExprParser.T__5)
                self.state = 113
                self.expr(0)
                self.state = 114
                self.match(ExprParser.T__6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 139
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.LogicalAndContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 118
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 119
                        self.match(ExprParser.AND)
                        self.state = 120
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.LogicalOrContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 121
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 122
                        self.match(ExprParser.OR)
                        self.state = 123
                        self.expr(16)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.EqualityContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 124
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 125
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==28):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 126
                        self.expr(15)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.RelationalContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 127
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 128
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 129
                        self.expr(14)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.MulDivModContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 130
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 131
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 132
                        self.expr(13)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.ShiftRightContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 133
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 134
                        self.match(ExprParser.SHR)
                        self.state = 135
                        self.expr(12)
                        pass

                    elif la_ == 7:
                        localctx = ExprParser.AddSubConcatContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 136
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 137
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8589940736) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 138
                        self.expr(11)
                        pass

             
                self.state = 143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 10)
         




