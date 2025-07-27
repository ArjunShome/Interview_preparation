

def maxSubsetSumNoAdjacent(array, index = 0, dum_array = None):
    # Write your code here.
    if len(array) == 0:
        return 0
    if dum_array is None:
        dum_array = []
    
    if index > len(array) - 1:
        return dum_array[-1]
    if index == 0:
        dum_array.append(array[0])
    elif index == 1:
        dum_array.append(max(array[0], array[1]))

    else:    
        dum_array.append(max(dum_array[index - 1], (dum_array[index - 2] + array[index])))
    return maxSubsetSumNoAdjacent(array, index + 1, dum_array)


if __name__ == '__main__':
    array = [4, 3, 5, 200, 5, 3]
    print(maxSubsetSumNoAdjacent(array))