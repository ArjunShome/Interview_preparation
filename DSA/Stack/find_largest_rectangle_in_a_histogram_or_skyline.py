
def largestRectangleUnderSkylineHistogram(buildings):
    max_rect_value = 0
    next_smaller_el = next_smaller(buildings)
    pre_smaller_el = pre_smaller(buildings)
    for i in range(len(buildings)):
        current_rect_value = buildings[i] * (next_smaller_el[i] - pre_smaller_el[i] - 1)
        max_rect_value = max(max_rect_value, current_rect_value)
    return max_rect_value


def next_smaller(array):
    stack = []
    output_array = [-1] * len(array)

    for i in range(len(array)-1, -1, -1):
        while stack and array[i] <= array[stack[-1]]:
            stack.pop()
        output_array[i] = stack[-1] if stack else len(array)
        stack.append(i)
    return output_array

def pre_smaller(array):
    stack = []
    output_array = [-1] * len(array)

    for i in range(len(array)):
        while stack and array[i] <= array[stack[-1]]:
            stack.pop()
        output_array[i] = stack[-1] if stack else -1
        stack.append(i)
    return output_array
    
if __name__ == '__main__':
    array = [1, 3, 3, 2, 4, 1, 5, 3, 2]
    print(largestRectangleUnderSkylineHistogram(array))