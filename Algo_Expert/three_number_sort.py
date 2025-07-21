def threeNumberSort(array, order):
    # Write your code here.
    i = 0
    for num in order:
        j = i+1
        while j < len(array):
            num1 = array[i]
            num2 = array[j]
            if num1 != num and num2 != num:
                j += 1
            elif num1 == num and num1 == num2:
                i = j
                j += 1
            elif num1 == num and num1 != num2:
                i += 1
                if j == i:
                    j += 1
            elif num2 == num:
                if num1 != num2:
                    temp = array[j]
                    array[j] = array[i]
                    array[i] = temp
                    i += 1
                    j += 1
            else:
                j += 1

    return array


if __name__ == '__main__':
    array = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 1, 2]
    order = [1, 2, 0]
    print(threeNumberSort(array, order)) 

