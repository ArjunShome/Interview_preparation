def reversePolishNotation(tokens):
    # Write your code here.
    stack = []
    result = 0

    if len(tokens) == 1:
        return int(tokens[0])
    
    for token in tokens:
        if token in ("+", "-", "*", "/"):
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operation(operand1, operand2, token)
            stack.append(result)
        else:
            stack.append(token)
    return result

def operation(operand1, operand2, operator_str):
    if operator_str == "-":
        return int(operand1) - int(operand2)
    if operator_str == "+":
        return int(operand1) + int(operand2)
    if operator_str == "*":
        return int(operand1) * int(operand2)
    if operator_str == "/":
        return int(int(operand1) / int(operand2))

if __name__ == '__main__':
    # tokens = ["3", "4", "+", "2", "/", "4", "-"]
    tokens = ["10", "-3", "/"]
    print(reversePolishNotation(tokens))