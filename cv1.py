def evaluate_expression(expression):
    def apply_operator(operand1, operator, operand2):
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            return operand1 / operand2

    def evaluate(expression):
        num_stack = []
        op_stack = []
        current_number = ""
        
        i = 0
        while i < len(expression):
            char = expression[i]
            
            if char.isdigit():
                current_number += char
            elif char == "(":
                open_brackets = 1
                j = i + 1
                while j < len(expression) and open_brackets > 0:
                    if expression[j] == "(":
                        open_brackets += 1
                    elif expression[j] == ")":
                        open_brackets -= 1
                    j += 1
                current_number = str(evaluate(expression[i + 1:j - 1]))
                i = j - 1
            else:
                if current_number:
                    num_stack.append(int(current_number))
                    current_number = ""
                if char in "+-*/":
                    while (op_stack and op_stack[-1] in "*/" and char in "+-") or (op_stack and op_stack[-1] in "*/" and char in "*/"):
                        num_stack.append(apply_operator(num_stack.pop(-2), op_stack.pop(), num_stack.pop()))
                    op_stack.append(char)
            
            i += 1
        
        if current_number:
            num_stack.append(int(current_number))
        
        while op_stack:
            num_stack.append(apply_operator(num_stack.pop(-2), op_stack.pop(), num_stack.pop()))
        
        return num_stack[0]

    return evaluate(expression)



num_operations = int(input("Zadej pocet operaci: "))
results = []

for x in range(num_operations):
    operation = input()
    
    try:
        operation = operation.replace(" ", "")
        result = evaluate_expression(operation)
        results.append(result)
    except Exception as e:
        results.append(f"Error: {e}")

for x in results:
    print(f"Result of operation: {x}")