def hasSingleCycle(array):
    # Write your code here.
    len_array = len(array)

    current_index= 0
    count = 0

    while count < len_array:
        if current_index == 0 and count > 0:
            return False
        count += 1
        num = array[current_index]
        index = current_index + num
        current_index = index % len_array

        if current_index < 0:
            current_index += len_array

    if current_index == 0:
        return True
    return False



if __name__ == '__main__':
    array = [3, 5, 6, -5, -2, -5, -12, -2, -1, 2, -6, 1, 1, 2, -5, 2]
    print(hasSingleCycle(array))