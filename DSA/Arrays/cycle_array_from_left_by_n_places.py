

class Array:
    def __init__(self, array):
        self.array = array
 
    def reverse(self, start, end):
        while start < end:
            temp = self.array[start]
            self.array[start] = self.array[end]
            self.array[end] = temp
            start +=1
            end -=1

    def rotate_left(self, n):
        self.reverse(0, n) # O(d)
        self.reverse(n + 1, len(self.array) - 1)  # O(n-d)
        self.reverse(0, len(self.array) - 1)  # O(n)
        return self.array 
    
    def rotet_right(self, n):
        self.reverse(len(self.array) - n, len(self.array))
        self.reverse(0, len(self.array) - n)
        self.reverse(0, len(self.array) - 1)
        return self.array
    
if __name__ == "__main__":
    input_array = input("Enter the array of numbers separated by comma: ")
    input_array = [int(number) for number in input_array.split(",")]
    n = int(input("Enter the number of places to rotate left: "))
    
    array_instance = Array(input_array)
    # rotated_array = array_instance.rotate_left(n)   # O(2n)
    right_rotated_array = array_instance.rotet_right(n)  # O(2n)
    # print(rotated_array)
    print(right_rotated_array)
    

        