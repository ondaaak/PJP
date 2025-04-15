grammar Expr;

// Parser rules
prog: command* EOF;

command: statement;

statement: ';'                                # EmptyStatement
         | expr ';'                           # ExprStatement
         | type ID (',' ID)* ';'              # Declaration
         | type ID '=' expr ';'               # DeclarationWithAssignment
         | 'read' ID (',' ID)* ';'            # ReadStatement
         | 'write' expr (',' expr)* ';'       # WriteStatement
         | '{' statement* '}'                 # BlockStatement
         | 'if' '(' expr ')' statement        # IfStatement
         | 'if' '(' expr ')' statement 'else' statement  # IfElseStatement
         | 'while' '(' expr ')' statement     # WhileStatement
         ;

type: 'int'                                  # IntType
    | 'float'                                # FloatType
    | 'bool'                                 # BoolType
    | 'string'                               # StringType
    ;

// Expression with operator precedence (from lowest to highest)
expr: expr '||' expr                         # LogicalOr
    | expr '&&' expr                         # LogicalAnd
    | expr ('==' | '!=') expr                # Equality
    | expr ('<' | '>' | '<=' | '>=') expr    # Relational
    | expr ('*' | '/' | '%') expr            # MulDivMod     // SWAP: Přehoďte toto pravidlo s pravidlem pro AddSubConcat
    | expr ('+' | '-' | '.') expr            # AddSubConcat
    | '!' expr                               # LogicalNot
    | '-' expr                               # UnaryMinus
    | <assoc=right> ID '=' expr              # Assignment
    | INT                                    # IntLiteral
    | FLOAT                                  # FloatLiteral
    | BOOL                                   # BoolLiteral
    | STRING                                 # StringLiteral
    | ID                                     # Variable
    | '(' expr ')'                           # Parens
    ;

// Lexer rules
// Keywords
IF: 'if';
ELSE: 'else';
WHILE: 'while';
READ: 'read';
WRITE: 'write';
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
BOOL_TYPE: 'bool';
STRING_TYPE: 'string';

// Operators
AND: '&&';
OR: '||';
NOT: '!';
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
CONCAT: '.';

BOOL: 'true' | 'false';
ID: [a-zA-Z][a-zA-Z0-9]*;      // Identifiers start with letter, can contain digits
INT: [0-9]+;                   // Integer literals
FLOAT: [0-9]+ '.' [0-9]*;      // Float literals with decimal point
STRING: '"' ( ~["\r\n\\] | '\\' . )* '"';  // String literals with optional escape sequences

// Handle whitespace and comments
WS: [ \t\r\n]+ -> skip;        // Skip whitespace
COMMENT: '//' ~[\r\n]* -> skip;  // Skip comments (// to end of line)