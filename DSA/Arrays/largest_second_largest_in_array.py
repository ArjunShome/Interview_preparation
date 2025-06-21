# Find the largest and second largest element in an array
import numpy as np

class Array:
    def __init__(self, array):
        self.array = array

    def find_largest(self):
        largest = self.array[0]
        for num in self.array:
            if num > largest:
                largest = num
        return largest
    
    def find_largest_second_largest_positive(self):
        largest = self.array[0]
        second_largest = -1
        for num in self.array:
            if num > second_largest and num < largest:
                second_largest = num
            if num > largest:
                second_largest = largest
                largest = num
        return largest, second_largest
    
    def find_largest_second_largest_negative(self):
        largest = self.array[0]
        second_largest = np.iinfo(np.int32).min
        for num in self.array:
            if num > second_largest and num < largest:
                second_largest = num
            if num > largest:
                second_largest = largest
                largest = num
        return largest, second_largest
    
    def find_smallest_second_smallest(self):
        smallest = self.array[len(self.array)-1]
        second_smallest = self.array[len(self.array)-2]
        for i in range(len(self.array)-1, 0, -1):
            if self.array[i] < second_smallest and self.array[i] > smallest:
                second_smallest = self.array[i]
            if self.array[i] < smallest:
                second_smallest = smallest
                smallest = self.array[i]
        return smallest, second_smallest

    
if __name__ == "__main__":
    input_array = input("Enter the array of numbers separated by comma: ")
    input_array = [int(number) for number in input_array.split(",")]
    array_instance = Array(input_array)
    
    if all(num >= 0 for num in input_array):
        largest, second_largest = array_instance.find_largest_second_largest_positive()
    else:
        largest, second_largest = array_instance.find_largest_second_largest_negative()

    smallest, second_smallest = array_instance.find_smallest_second_smallest()
    
    print(f"Largest: {largest}, Second Largest: {second_largest}, Smallest: {smallest}, Second Smallest: {second_smallest}")