
# def nextGreaterElement(array):
#     # Write your code here.
#     stack = []
#     output_array = []
#     for i in range(len(array)):
#         stack.append(array[i])

#         element = stack[-1] 
#         # find the next largest element
#         j = i + 1
#         iter_count = 0
#         # Convert to recursion
#         while True:
#             if iter_count == len(array) - 1:
#                 output_array.append(-1)
#                 break
#             if j == len(array):
#                 j = 0
#             if element < array[j]:
#                 index = j % len(array)
#                 output_array.append(array[index])
#                 break
#             else:
#                 j += 1
#             iter_count += 1
        
#     return output_array


def nextGreaterElement(array):
    n = len(array)
    result = [-1] * n
    stack = []

    for i in range(2 * n):
        current_index = i % n
        current_value = array[current_index]

        while stack and array[stack[-1]] < current_value:
            idx = stack.pop()
            result[idx] = current_value

        if i < n:
            stack.append(i)

    return result

if __name__ == '__main__':
    array = [2 , 5, -3, -4, 6, 7, 2]
    print(nextGreaterElement(array)) 