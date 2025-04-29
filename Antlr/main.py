from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.syntax_errors = []
        
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error = f"Syntax error at line {line}, column {column}: {msg}"
        self.syntax_errors.append(error)

def main():
    input_text = """
write "<Constants>";
write "10: ",10;
write " 1.25: ", 1.25;
write "";;

write "<Variables>";
string s;
s="Abcd";
write "s(Abcd): ", s;

float d;
d=3.141592;
write "d(3.141592): ", d;

int n;
n=-500;
write "n(-500): ", n;
write "";

bool boolean;
boolean=true;
write "boolean(true): ",boolean;
write "";

write "<Expressions>";
write "2+3*5(17): ",2+3*5;
write "17 / 3(5): ", 17 / 3;
write "17 % 3(2): ", 17 % 3;
write "2.5*2.5/6.25(1.0): ", 2.5*2.5/6.25;
write "1.5*3(4.5): ", 1.5*3;
write "abc+def (abcdef): ", "abc"."def";
write "";

write  "<Comments>"; // hidden
// write  "it is error, if you see this";

write "<Automatic int conversion>";
float y;
y = 10;
write "y (10.0): ", y;

write "<Multiple Assignments>";
int i,j,k;
i=j=k=55;
write "i=j=k=55: ",i,"=",j,"=",k;

write "<Input - a(int),b(float),c(string),d(bool)>";
int a;
float b;
string c;
bool e;
a = 0;
b = 0.0;
c = "";
e = true;
read a,b,c,e;
write "a,b,c,e: ", a, ",", b, ",", c, ",",e;
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
    
    # Generate code
    from CodeGenVisitor import CodeGenVisitor
    codegen = CodeGenVisitor()
    code = codegen.visit(tree)

    with open("output.asm", "w", encoding="utf-8") as f:
        for line in code:
            f.write(line + "\n")
    print("Target code generated in output.asm")

if __name__ == '__main__':
    main()