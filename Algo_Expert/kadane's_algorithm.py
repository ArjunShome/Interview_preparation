def kadanesAlgorithm(array):
    # Write your code here.
    max_sum = 0
    sum = 0
    if len(array) == 1:
        return array[0]
    for i in range(len(array)):
        # Check negatives, then reset
        if sum + array[i] < 0:
            sum = 0
        # If the currentsum is bigger thn sum then only add sum
        else:
            sum += array[i]            
        max_sum = max(max_sum, sum)
    return max_sum if max_sum else -1



if __name__ == '__main__':
    array = [-1000, -1000, 2, 4, -5, -6, -7, -8, -2, -100]
    print(kadanesAlgorithm(array))  # Expected output: 19
