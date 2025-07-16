

def threeNumberSum(array, targetSum):
    array.sort()
    final_array = []
    for i in range(len(array)):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == targetSum:
                final_array.append([array[i], array[left], array[right]])
                right -= 1
                left += 1
            elif current_sum < targetSum:
                left += 1
            else:
                right -= 1
    return final_array



if __name__ == '__main__':
    # array = [12,3,1,2,-6,5,-8,6]
    array = [1,2,3]
    target_sum = 6
    print(threeNumberSum(array, target_sum))