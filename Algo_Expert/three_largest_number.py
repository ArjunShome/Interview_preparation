
def findThreeLargestNumbers(array):
    # Write your code here.
    final_array = [-float('inf'), -float('inf'), -float('inf')]
    for num in array:
        if num > final_array[0]:
            final_array[2] = final_array[1]
            final_array[1] = final_array[0]
            final_array[0] = num
        elif num > final_array[1]:
            final_array[2] = final_array[1]
            final_array[1] = num
        elif num > final_array[2]:
            final_array[2] = num
    return final_array[:: -1]
    


if __name__ == '__main__':
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    sorted_array = [-27, -17, -7, 1, 7, 7, 8, 17, 18, 141, 541]
    print(findThreeLargestNumbers(array))
