grammar Expr;

// Parser rules
prog: command* EOF;

command: statement;

statement: ';'                                # EmptyStatement
         | expr ';'                           # ExprStatement
         | ID '=' expr ';'                    # Assignment
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

expr: expr op=('*'|'/') expr                 # MulDiv
    | expr op=('+'|'-') expr                 # AddSub
    | expr op=('<'|'>'|'<='|'>='|'=='|'!=') expr  # Comparison
    | expr op=('&&'|'||') expr               # LogicalOp
    | '!' expr                               # NotOp
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

BOOL: 'true' | 'false';
ID: [a-zA-Z][a-zA-Z0-9]*;      // Identifiers start with letter, can contain digits
INT: [0-9]+;                   // Integer literals
FLOAT: [0-9]+ '.' [0-9]*;      // Float literals with decimal point
STRING: '"' ( ~["\r\n\\] | '\\' . )* '"';  // String literals with optional escape sequences

// Handle whitespace and comments
WS: [ \t\r\n]+ -> skip;        // Skip whitespace
COMMENT: '//' ~[\r\n]* -> skip;  // Skip comments (// to end of line)