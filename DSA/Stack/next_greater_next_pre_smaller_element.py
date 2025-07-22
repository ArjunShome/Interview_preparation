
def next_greater_elements(array):
    stack = []
    output_array = [-1] * len(array)
    for i in range(len(array)-1, -1, -1):
        if stack:
            while stack and array[i] >= stack[-1]:
                stack.pop()
            if not stack:
                stack.append(array[i])
                continue
            if array[i] < stack[-1]:
                output_array[i] = stack[-1]
                stack.append(array[i])
        else:
            stack.append(array[i])
    return output_array


def next_smaller_elements(array):
    stack = []
    output_array = [-1] * len(array)
    for i in range(len(array)-1, -1, -1):
        if stack:
            while stack and array[i] <= stack[-1]:
                stack.pop()
            if not stack:
                stack.append(array[i])
                continue
            if array[i] > stack[-1]:
                output_array[i] = stack[-1]
                stack.append(array[i])
        else:
            stack.append(array[i])
    return output_array

def pre_smaller_elements(array):
    stack = []
    output_array = [-1] * len(array)
    for i in range(0, len(array)-1):
        if stack:
            while stack and array[i] <= stack[-1]:
                stack.pop()
            if not stack:
                stack.append(array[i])
                continue
            if array[i] > stack[-1]:
                output_array[i] = stack[-1]
                stack.append(array[i])
        else:
            stack.append(array[i])
    return output_array


if __name__ == '__main__':
    array = [4,12,5,3,1,2,5,3,1,2,4,6]
    print(next_greater_elements(array))
    print(next_smaller_elements(array))
    print(pre_smaller_elements(array))