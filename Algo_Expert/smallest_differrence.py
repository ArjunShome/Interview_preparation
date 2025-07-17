
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    i = 0
    j = 0
    smallest_pair = []
    diff = float('inf')

    while i <= len(arrayOne) - 1 and j <= len(arrayTwo) - 1:
        current_diff = abs(arrayOne[i] - arrayTwo[j])
        if current_diff <= diff:
            diff = current_diff
            smallest_pair = [arrayOne[i], arrayTwo[j]]
        
        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else:
            j += 1

    return smallest_pair




if __name__ == '__main__':
    array_1 =  [-1, 5, 10, 20, 28, 3]  # [0,  10,  20,  25,  2000]
    array_2 = [26, 134, 135, 15, 17] # [1005, 1006, 1014, 1031, 1032]

    print(smallestDifference(array_1, array_2)) 

