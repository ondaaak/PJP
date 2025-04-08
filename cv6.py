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
            continue
        elif ch.isdigit():
            start = i
            while i < len(expression) and expression[i].isdigit():
                i += 1
            tokens.append(Token('NUM', int(expression[start:i])))
            continue
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
        self.error_occurred = False

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, kind=None):
        token = self.current_token()
        if token and (kind is None or token.kind == kind):
            self.pos += 1
            return token
        self.error_occurred = True
        return None

    def E(self):
        """ E : T E1 """
        value = self.T()
        if value is None or self.error_occurred:
            return None
        return self.E1(value)

    def E1(self, left_value):
        """ E1 : '+' T E1 | '-' T E1 | {e} """
        token = self.current_token()
        if token and token.kind in ['+', '-']:
            op = token.kind
            self.consume(op)
            right_value = self.T()
            if right_value is None or self.error_occurred:
                return None
            if op == '+':
                left_value += right_value
            else:
                left_value -= right_value
            return self.E1(left_value)
        return left_value

    def T(self):
        """ T : F T1 """
        value = self.F() 
        if value is None or self.error_occurred:
            return None
        return self.T1(value)

    def T1(self, left_value):
        """ T1 : '*' F T1 | '/' F T1 | {e} """
        token = self.current_token()
        if token and token.kind in ['*', '/']:
            op = token.kind
            self.consume(op)
            right_value = self.F() 
            if right_value is None or self.error_occurred:
                return None
            if op == '*':
                left_value *= right_value
            else:
                if right_value == 0:
                    self.error_occurred = True
                    return None
                else:
                    left_value //= right_value
            return self.T1(left_value)
        return left_value

    def F(self):
        """ F : '(' E ')' | num """
        token = self.current_token()
        if not token:
            self.error_occurred = True
            return None
            
        if token.kind == '(':
            self.consume('(')
            value = self.E()
            if value is None or not self.consume(')'):
                self.error_occurred = True
                return None
            return value
        elif token.kind == 'NUM':
            value = token.value
            self.consume('NUM')
            return value
        else:
            self.error_occurred = True
            return None

def evaluate_expression(expr):
    tokens = tokenize(expr)
    if not tokens:
        return None
    parser = Parser(tokens)
    value = parser.E()

    if parser.error_occurred or parser.current_token().kind != 'EOF':
        return None
    return value

def main():
    try:
        N = int(input())
        
        for _ in range(N):
            expr = input()
            result = evaluate_expression(expr)
            if result is None:
                print("ERROR")
            else:
                print(result)
    except Exception:
        print("ERROR")

if __name__ == "__main__":
    main()