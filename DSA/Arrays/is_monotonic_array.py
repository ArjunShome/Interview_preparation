def isMonotonic(array):
    # Write your code here.
    if not array:
        return True
    if len(array) == 1:
        return True

    first = 0
    last = len(array) - 1
    flag = False
    i = 0
    while i < len(array) - 1:
        if array[first] == array[last]:
            first += 1
            last -= 1
            continue
        if array[first] >= array[last] and array[i] >= array[i + 1]:
            flag = True
        elif array[first] <= array[last] and array[i] <= array[i + 1]:
            flag = True
        else:
            return False
        i += 1
    
    return flag

if __name__ == '__main__':
    array = [1, 1, 1, 2, 3, 4, 1]
    # array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
    print(isMonotonic(array=array))
