from antlr4 import *
from ExprLexer import exprLexer
from ExprParser import exprParser
from EvalVisitor import EvalVisitor

visitor = EvalVisitor()

print("PLC Expr REPL â€“ zadej vĂ˝raz nebo pĹ™iĹ™azenĂ­ (Ctrl+C pro ukonÄŤenĂ­):")
while True:
    try:
        line = input('>> ')
        input_stream = InputStream(line + '\n')  # NEWLINE je souÄŤĂˇst syntaxe!
        lexer = exprLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = exprParser(tokens)
        tree = parser.stat()
        result = visitor.visit(tree)
        if result is not None:
            print(result)
    except KeyboardInterrupt:
        print("\nBye!")
        break
    except Exception as e:
        print("Chyba:", e)