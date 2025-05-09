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
write "<Relational operators>";
write "1<5: ", 1 < 5;
write "1>3.5: ", 1 > 3.5;
write "aa==aa: ", "aa"=="aa";
write "aa==ab: ", "aa"=="ab";
write "aa!=ab: ", "aa"!="ab";
write "";
write "<Logic operators>";
write "false and true (false):", false && true;
write "false or true (true):", false || true;
write "not 1==2 (true):", !(1==2);
write "true or false and true (true):", true || false && true;
"""
    
    input_stream = InputStream(input_text)
    
    lexer = ExprLexer(input_stream)
    error_listener = SyntaxErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    
    tokens = CommonTokenStream(lexer)
    
    parser = ExprParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.prog()
    
    if error_listener.syntax_errors:
        print("Syntax errors detected:")
        for error in error_listener.syntax_errors:
            print(f"  {error}")
        return
    
    visitor = EvalVisitor()
    results = visitor.visit(tree)
    
    if visitor.type_errors:
        print("Type errors detected:")
        for error in visitor.type_errors:
            print(f"  {error}")
        return
    
    print("Results:")
    for r in results:
        if r is not None:
            print(r)

    print("\nVariable values from visitor:")
    for key, value in visitor.memory.items():
        print(f"{key}: {value} (type: {visitor.types.get(key, 'unknown')})")
    
    from CodeGenVisitor import CodeGenVisitor
    codegen = CodeGenVisitor()
    code = codegen.visit(tree)

    with open("output.asm", "w", encoding="utf-8") as f:
        for line in code:
            f.write(line + "\n")
    print("Target code generated in output.asm")

if __name__ == '__main__':
    main()