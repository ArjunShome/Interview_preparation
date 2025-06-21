# Implement Sorting using Selection Sort.

def swap(num_array, smaller_indx, larger_indx):
    temp = num_array[larger_indx]
    num_array[larger_indx] = num_array[smaller_indx]
    num_array[smaller_indx] = temp


def sort_data_using_selection_sort(num_array):
    for i in range(len(num_array)-1):
        for j in range(i+1, len(num_array)):
            if num_array[i] > num_array[j]:
                swap(num_array, i, j)
    return num_array
        


if __name__=="__main__":
    numbers = input("Enter the random array seperated by comma: ")
    numbers = [int(number) for number in numbers.split(",")]
    numbers = sort_data_using_selection_sort(numbers)
    print(numbers)

