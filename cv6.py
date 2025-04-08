import sys

class Token:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value

def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        ch = expression[i]
        if ch.isspace():
            i += 1
        elif ch.isdigit():
            start = i
            while i < len(expression) and expression[i].isdigit():
                i += 1
            tokens.append(Token('NUM', int(expression[start:i])))
        elif ch in '+-*/()':
            tokens.append(Token(ch, ch))
            i += 1
        else:
            return None
    tokens.append(Token('EOF', None))
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.error = False

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, kind=None):
        token = self.current()
        if token and (kind is None or token.kind == kind):
            self.pos += 1
            return token
        self.error = True
        return None

    def E(self):
        """ E : T E1 """
        value = self.T()
        return self.E1(value)

    def E1(self, left):
        """ E1 : '+' T E1 | '-' T E1 | {e} """
        token = self.current()
        if token and token.kind in ['+', '-']:
            op = token.kind
            self.eat(op)
            right = self.T()
            if op == '+': 
                left += right
            else: 
                left -= right
            return self.E1(left)
        return left

    def T(self):
        """ T : F T1 """
        value = self.F()
        return self.T1(value)

    def T1(self, left):
        """ T1 : '*' F T1 | '/' F T1 | {e} """
        token = self.current()
        if token and token.kind in ['*', '/']:
            op = token.kind
            self.eat(op)
            right = self.F()
            if op == '*': 
                left *= right
            else:
                if right == 0:
                    self.error = True
                    return None
                left //= right
            return self.T1(left)
        return left

    def F(self):
        """ F : '(' E ')' | num """
        token = self.current()
        if token.kind == '(':
            self.eat('(')
            value = self.E()
            self.eat(')')
            return value
        else: 
            value = token.value
            self.eat('NUM')
            return value

def evaluate(expr):
    tokens = tokenize(expr)
    if not tokens:
        return None
    
    parser = Parser(tokens)
    result = parser.E()
    
    if parser.error or parser.current().kind != 'EOF':
        return None
    
    return result

def main():
    try:
        N = int(input())
        for _ in range(N):
            expr = input()
            result = evaluate(expr)
            if result is None:
                print("ERROR")
            else:
                print(result)
    except:
        print("ERROR")

if __name__ == "__main__":
    main()