class Array:
    def __init__(self, array):
        self.array = array

    def move_zeros_at_end(self):
        i = 0
        for j in range(len(self.array)):
            if self.array[j] == 0:
                continue
            else:
                temp = self.array[i]
                self.array[i] = self.array[j]
                self.array[j] = temp
                i += 1
        return self.array
    
if __name__ == "__main__":
    input_array = input("Enter the array of numbers separated by comma: ")
    input_array = [int(number) for number in input_array.split(",")]
    
    array_instance = Array(input_array)
    moved_array = array_instance.move_zeros_at_end()
    print(moved_array)