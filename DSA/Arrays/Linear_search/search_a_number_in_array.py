
class Array:
    def __init__(self, array):
        self.array = array

    def linear_search_first_instance(self, number):
        for i in range(len(self.array)):
            if self.array[i] == number:
                return i
        return -1
        
    def linear_search_last_instance(self, number):
        for i in range(len(self.array)-1, 0, -1):
            if self.array[i] == number:
                return i
        return -1
        
    def linear_search_all_instance(self, number):
        instances = []
        for i in range(len(self.array)):
            if self.array[i] == number:
                instances.append(i)
        if len(instances) == 0:
            return -1
        return instances
    

if __name__ == "__main__":
    input_array = input("Enter the array of numbers separated by comma: ")
    input_array = [int(number) for number in input_array.split(",")]
    number_to_search = int(input("Enter the number to search in the array: "))
    
    array_instance = Array(input_array)
    first_instance = array_instance.linear_search_first_instance(number_to_search)
    last_instance = array_instance.linear_search_last_instance(number_to_search)
    all_instances = array_instance.linear_search_all_instance(number_to_search)
    
    print(f"First instance of {number_to_search}: {first_instance}")
    print(f"Last instance of {number_to_search}: {last_instance}")
    print(f"All instances of {number_to_search}: {all_instances}")