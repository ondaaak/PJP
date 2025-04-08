from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor
from EvalListener import EvalListener

def main():
    #input_text = input("Enter expression or assignment: ")
    input_text = """
a = 3;
b = 4;
a + b * 2;
(1 + 2) * 3;
"""
    input_stream = InputStream(input_text)
    lexer = ExprLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)

    tree = parser.prog()
    visitor = EvalVisitor()
    results = visitor.visit(tree)

    for r in results:
        print(r)

    listener = EvalListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    for key, value in listener.values.items():
        print(f"{key}: {value}")

if __name__ == '__main__':
    main()