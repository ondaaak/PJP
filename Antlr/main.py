from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor
from EvalListener import EvalListener

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.syntax_errors = []
        
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error = f"Syntax error at line {line}, column {column}: {msg}"
        self.syntax_errors.append(error)

def main():
    #input_text = input("Enter expression or assignment: ")
    input_text = """
// This is a comment
// Testing variable declarations
int intVar;             // Declaration with default value (0)
float floatVar;         // Declaration with default value (0.0)
bool boolVar;           // Declaration with default value (false)
string stringVar;       // Declaration with default value ("")

// Testing declarations with assignment
int x = 42;             // Integer declaration with assignment
float y = 3.14;         // Float declaration with assignment
bool flag = true;       // Boolean declaration with assignment
string message = "Hello, World!";  // String declaration with assignment

// Test expressions with declared variables
intVar = 10;            // Assign value to declared variable
x + intVar;             // Expression using declared variables
y * 2;                  // Float arithmetic

// Test string operations
string s1 = "Concatenate ";
string s2 = "strings";
s1 + s2;                // String concatenation
"""
    input_stream = InputStream(input_text)
    
    # Setup lexer with error handling
    lexer = ExprLexer(input_stream)
    error_listener = SyntaxErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    
    tokens = CommonTokenStream(lexer)
    
    # Setup parser with error handling
    parser = ExprParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    # Parse and check for syntax errors
    tree = parser.prog()
    
    if error_listener.syntax_errors:
        print("Syntax errors detected:")
        for error in error_listener.syntax_errors:
            print(f"  {error}")
        return
    
    # Use visitor for semantic analysis and evaluation
    visitor = EvalVisitor()
    results = visitor.visit(tree)
    
    # Check for type errors
    if visitor.type_errors:
        print("Type errors detected:")
        for error in visitor.type_errors:
            print(f"  {error}")
        return
    
    # If no errors, print results
    print("Results:")
    for r in results:
        if r is not None:
            print(r)

    print("\nVariable values from visitor:")
    for key, value in visitor.memory.items():
        print(f"{key}: {value} (type: {visitor.types.get(key, 'unknown')})")

    # Also demonstrate listener-based approach
    listener = EvalListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print("\nVariable values from listener:")
    for key, value in listener.values.items():
        print(f"{key}: {value} (type: {listener.types.get(key, 'unknown')})")

if __name__ == '__main__':
    main()