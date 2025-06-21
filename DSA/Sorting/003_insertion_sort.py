
def swap(num_array, smaller_indx, larger_indx):
    temp = num_array[larger_indx]
    num_array[larger_indx] = num_array[smaller_indx]
    num_array[smaller_indx] = temp

def insertion_sort(array):
    for i in range(len(array) - 1):
        j = i
        while (j > 0 and array[j - 1] > array[j]):
            swap(array, j , j-1)
            j -= 1
    return array

if __name__=='__main__':
    array = input("Enter the array of numbers seperated by comma: ")
    array = [int(number) for number in array.split(",")]
    array = insertion_sort(array)
    print(array)