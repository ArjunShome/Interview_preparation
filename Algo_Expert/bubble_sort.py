

def bubbleSort(array):
    # Write your code here.
    n = len(array) - 1
    i = 0
    while i <= n:
        swapped = False
        for j in range(i, n):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swapped = True
        if not swapped:
            break
        n -= 1                
    return array




if __name__ == '__main__':
    array = [8, 5, 2, 9, 5, 6, 3]
    print(bubbleSort(array))