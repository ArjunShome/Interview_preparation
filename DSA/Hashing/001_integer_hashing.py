

class HashFindIntegerUsingDict:
    def __init__(self, array: list[int]):
        """
        Initialize the HashFindIntegerUsingDict class with an array of integers
        Operations - 
        1. Count the number of times a number appear in tha array.
        """
        self.num_array = array
        self.hash_table = {}
        self._create_hash()
        self._preload_hash()

    def _create_hash(self):
        """
        Create a hash table using dictionary from the array size.
        """
        hash_max_value = max(self.num_array) + 1
        hash_min_value = min(self.num_array)
        # Initialize the hash table with zeros
        for i in range(hash_min_value, hash_max_value):
            self.hash_table[i] = 0

    def _preload_hash(self):
        """
        Preload the hash table with the number of times each number appears in the array.
        """
        for index in self.num_array:
            self.hash_table[index] += 1

    def find(self, number: int) -> int:
        """
        Find the number of times a number appears in the array.
        """
        return self.hash_table[number]
    


from collections import Counter

class HashArrayFindIntegerCounter:
    def __init__(self, array):
        self.array = array
        self.hash_array = Counter(self.array)

    def find(self, number: int):
        return self.hash_array[number]



if __name__ == "__main__":
    input_array = input("Enter the array of numbers split by comma: ")
    array = [int(num) for num in input_array.split(',')]

    # hash_finder = HashFindIntegerUsingDict(array)
    hash_finder = HashArrayFindIntegerCounter(array)
    
    while(True):
        number_to_find = int(input("Enter the number to find: "))
        if number_to_find == -1:
            break
        else:
            print(f"The Number {number_to_find} appears {hash_finder.find(number_to_find)} times")
        

