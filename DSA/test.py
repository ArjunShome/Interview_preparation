def sortedSquaredArray(array):
    left = 0
    right = len(array) - 1
    final_lst  = [0] * len(array)

    while left <= right:
        
        if left == right:
            final_lst[0] = (array[left] * array[left])
            break

        if (array[left] * array[left]) > (array[right] * array[right]):
            final_lst[right - left] = (array[left] * array[left])
            left += 1
        else:
            final_lst[right - left] = (array[right] * array[right])
            right -= 1
    return final_lst



if __name__ == "__main__":
    array = [-10, -5, 0, 5, 10]
    print(sortedSquaredArray(array=array))