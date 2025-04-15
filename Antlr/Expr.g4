grammar Expr;

// Parser rules
prog: command* EOF;

command: statement;

statement: expr ';'                          # ExprStatement
         | ID '=' expr ';'                   # Assignment
         | type ID ';'                       # Declaration
         | type ID '=' expr ';'              # DeclarationWithAssignment
         ;

type: 'int'                                  # IntType
    | 'float'                                # FloatType
    | 'bool'                                 # BoolType
    | 'string'                               # StringType
    ;

expr: expr op=('*'|'/') expr                 # MulDiv
    | expr op=('+'|'-') expr                 # AddSub
    | INT                                    # IntLiteral
    | FLOAT                                  # FloatLiteral
    | BOOL                                   # BoolLiteral
    | STRING                                 # StringLiteral
    | ID                                     # Variable
    | '(' expr ')'                           # Parens
    ;

// Lexer rules
// Keywords
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
BOOL_TYPE: 'bool';
STRING_TYPE: 'string';

BOOL: 'true' | 'false';
ID: [a-zA-Z][a-zA-Z0-9]*;      // Identifiers start with letter, can contain digits
INT: [0-9]+;                   // Integer literals
FLOAT: [0-9]+ '.' [0-9]*;      // Float literals with decimal point
STRING: '"' ( ~["\r\n\\] | '\\' . )* '"';  // String literals with optional escape sequences

// Handle whitespace and comments
WS: [ \t\r\n]+ -> skip;        // Skip whitespace
COMMENT: '//' ~[\r\n]* -> skip;  // Skip comments (// to end of line)