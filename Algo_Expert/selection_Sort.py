
def selectionSort(array):
    # Write your code here.
    cur_idx = 0
    while cur_idx < len(array) - 1:
        smallest_idx = cur_idx
        for i in range(cur_idx + 1, len(array)):
            if array[smallest_idx] > array[i]:
                smallest_idx = i
        temp = array[cur_idx]
        array[cur_idx] = array[smallest_idx]
        array[smallest_idx] = temp
        cur_idx += 1
    return array

if __name__ == '__main__':
    array = [8, 5, 2, 9, 5, 6, 3]
    print(selectionSort(array))