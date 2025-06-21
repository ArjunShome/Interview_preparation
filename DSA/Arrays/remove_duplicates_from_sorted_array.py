# Remove duplicates from an array which is already sorted..
class Array:
    def __init__(self, array):
        self.array = array

    def remove_duplicates_using_set(self):
        self.array = set(self.array)
        return self.array
    
    def remove_duplicates_without_using_set(self):
        i = 0
        for j in range(1, len(self.array)):
            if self.array[j] != self.array[i]:
                self.array[i+1] = self.array[j]
                i +=1 
        return self.array[:i+1]
    
if __name__ == "__main__":
    input_array = input("Enter the array of numbers separated by comma: ")
    input_array = [int(number) for number in input_array.split(",")]
    array_instance = Array(input_array)
    # unique_array = array_instance.remove_duplicates_using_set()
    unique_array = array_instance.remove_duplicates_without_using_set()
    print(unique_array)