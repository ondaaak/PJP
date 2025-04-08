import sys

class Token:
    def __init__(self, kind, value):
        self.kind = kind  # e.g., 'NUM', '+', '-', '*', '/', '(', ')', 'EOF'
        self.value = value

def tokenize(expression):
    """ Simple tokenizer splitting on operators and digits. """
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
            # Invalid character
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

    def parse_expression(self):
        """ E : T E1 """
        value = self.parse_term()
        if value is None or self.error_occurred:
            return None
        return self.parse_expression_tail(value)

    def parse_expression_tail(self, left_value):
        """ E1 : '+' T E1 | '-' T E1 | {e} """
        token = self.current_token()
        if token and token.kind in ['+', '-']:
            op = token.kind
            self.consume(op)
            right_value = self.parse_term()
            if right_value is None or self.error_occurred:
                return None
            if op == '+':
                left_value += right_value
            else:
                left_value -= right_value
            return self.parse_expression_tail(left_value)
        return left_value

    def parse_term(self):
        """ T : F T1 """
        value = self.parse_factor()
        if value is None or self.error_occurred:
            return None
        return self.parse_term_tail(value)

    def parse_term_tail(self, left_value):
        """ T1 : '*' F T1 | '/' F T1 | {e} """
        token = self.current_token()
        if token and token.kind in ['*', '/']:
            op = token.kind
            self.consume(op)
            right_value = self.parse_factor()
            if right_value is None or self.error_occurred:
                return None
            if op == '*':
                left_value *= right_value
            else:
                # Check for divide by zero
                if right_value == 0:
                    self.error_occurred = True
                    return None
                else:
                    left_value //= right_value
            return self.parse_term_tail(left_value)
        return left_value

    def parse_factor(self):
        """ F : '(' E ')' | num """
        token = self.current_token()
        if not token:
            self.error_occurred = True
            return None
            
        if token.kind == '(':
            self.consume('(')
            value = self.parse_expression()
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
    value = parser.parse_expression()

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
    