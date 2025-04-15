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
// Testing different literal types
intVar = 42;           // Integer literal
floatVar = 3.14;       // Float literal
boolVar = true;        // Boolean literal
stringVar = "Hello, World!";  // String literal

// Test expressions
intVar + 10;           // Integer arithmetic
floatVar * 2;          // Float arithmetic
"Concatenate " + "strings";  // String concatenation

// Test more complex expressions
(intVar + floatVar) * 2;
boolVar = false;
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