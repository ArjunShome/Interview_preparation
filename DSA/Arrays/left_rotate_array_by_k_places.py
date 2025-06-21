
class Array:
    def __init__(self, array):
        self.array = array

    def rotate_arr_by_k_places_left(self, k):
        main_array = self.array[k:]
        array_len = len(main_array) + 1
        rotate_arr = self.array[:k]

        for i in range(len(rotate_arr)):
            main_array.append(rotate_arr[i])
            array_len += 1
        
        return main_array

    def rotate_arr_by_k_places_right(self, k):
        main_len = len(self.array) - k
        main_array = self.array[: main_len]
        rotate_arr = self.array[main_len:]

        main_array = rotate_arr + main_array
        
        return main_array
            
if __name__ == "__main__":
    input_array = input("Enter the array of numbers separated by comma: ")
    input_array = [int(number) for number in input_array.split(",")]
    k = int(input("Enter the number of places to rotate left: "))
    
    array_instance = Array(input_array)
    rotated_array = array_instance.rotate_arr_by_k_places_left(k)
    rotated_array_right = array_instance.rotate_arr_by_k_places_right(k)
    print(rotated_array)
    print(rotated_array_right)
            