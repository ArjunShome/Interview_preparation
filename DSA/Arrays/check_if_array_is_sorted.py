
class IsArraySorted():
    def __init__(self, array):
        self.array = array

    def check_is_sorted(self):
        sorted = True
        for i in range(len(self.array)-1):
            if self.array[i] <= self.array[i + 1]:
                continue
            else:
                sorted = False
                break
        return sorted
    

if __name__ == "__main__":
    input_array = input("Enter the array of numbers separated by comma: ")
    input_array = [int(number) for number in input_array.split(",")]
    is_sorted_instance = IsArraySorted(input_array)
    is_sorted = is_sorted_instance.check_is_sorted()
    if is_sorted:
        print("The array is sorted.")
    else:
        print("The array is not sorted.")