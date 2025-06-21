# Quick Sort Algorithm.

class QuickSort:
        def __init__(self):
            pass

        def quick_sort(self,array, low, high):
            if low < high:
                pIndex = self.get_partition_index(array, low, high)
                self.quick_sort(array, low, pIndex-1)
                self.quick_sort(array, pIndex + 1, high)
            return array

        def get_partition_index(self, array, low, high):
            i = low
            j = high
            pivot = array[low]
            while (i< j):
                while(array[i] <= pivot and i <= high-1):
                    i+=1
                while(array[j] > pivot and j >= low+1):
                    j-=1
                if (i < j):
                    self.swap(array, i, j)
            self.swap(array, low, j)
            return j

        def swap(self, array, low, high):
            temp = array[low]
            array[low] = array[high]
            array[high] = temp


if __name__ == "__main__":
    input_array = input("Enter the array of numbers separated by comma: ")
    input_array = [int(number) for number in input_array.split(",")]
    quick_sort = QuickSort()
    sorted_array = quick_sort.quick_sort(input_array, 0, len(input_array) - 1)
    print(sorted_array)


    
