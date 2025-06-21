def swap(num_array, smaller_indx, larger_indx):
    temp = num_array[larger_indx]
    num_array[larger_indx] = num_array[smaller_indx]
    num_array[smaller_indx] = temp

def bubble_sort(numbers): # Complexity - O(n2) -> Worst case, O(n) -> Best Case
    loop = len(numbers)
    is_swapped = 0
    for i in (range(loop)):
        for j in (range(0, loop - i - 1)):
            first = numbers[j]
            second = numbers[j+1]
            if first > second:
                swap(numbers, j+1, j)
                is_swapped = 1
        if not is_swapped:
            return numbers
    return numbers


if __name__ == "__main__":
    numbers = input("Enter the number to sort comma seperated: ")
    numbers = [int(number) for number in numbers.split(",")]
    print(bubble_sort(numbers))