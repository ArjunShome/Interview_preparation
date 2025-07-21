

def bestDigits(number, numDigits):
    stack = []
    for digit in number:
        while stack and numDigits > 0 and stack[-1] < digit:
            stack.pop()
            numDigits -= 1
        stack.append(digit)

    # If still digits to remove, cut from end
    return ''.join(stack[:-numDigits]) if numDigits else ''.join(stack)

if __name__ == '__main__':
    number = "462839"
    numDigits = 2

    print(bestDigits(number, numDigits))