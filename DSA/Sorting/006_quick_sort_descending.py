# Write a Quick sort logic to sort an array in descending order.

class QuickSortDesc:

    def quick_sort(self, array, low, high):
        if low < high:
            p_index = self.get_partition_index(array, low, high)
            self.quick_sort(array, low, p_index - 1)
            self.quick_sort(array, p_index + 1, high)
        return array
    
    def get_partition_index(self, array, low, high):
        pivot = array[low]
        i = low
        j = high

        while i < j:
            while array[i] >= pivot and i <= high - 1:
                i +=1
            while array[j] <= pivot and j >= low + 1:
                j -= 1
            
            if i < j:
                self.swap(array, i, j)
        self.swap(array, low, j)
        return j
    
    def swap(self, num_array, larger_indx, smaller_indx):
        temp = num_array[larger_indx]
        num_array[larger_indx] = num_array[smaller_indx]
        num_array[smaller_indx] = temp


if __name__ == "__main__":
    input_array = input("Enter the array of numbers separated by comma: ")
    input_array = [int(number) for number in input_array.split(",")]
    quick_sort_desc = QuickSortDesc()
    sorted_array = quick_sort_desc.quick_sort(input_array, 0, len(input_array) - 1)
    print(sorted_array)