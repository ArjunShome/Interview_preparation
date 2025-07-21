
def sortStack(stack):
    # Write your code here.
    if len(stack) > 1:
        first_top_element = stack.pop()
        sortStack(stack)
        insertStack(stack, first_top_element)
    return stack

def insertStack(stack, element):
    if not stack:
        stack.append(element)
        return
    if element < stack[-1]:
        top = stack.pop()
        insertStack(stack, element)
        stack.append(top)
        return
    stack.append(element)
    return

if __name__ == '__main__':
    # stack = [-5, 2, -2, 4, 3, 1]
    stack = [3, 4, 5, 1, 2]
    print(sortStack(stack))