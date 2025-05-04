
class HashFindStr():
    """
    _summary_
    A class to count the number of times each character appears in a list of strings using string hashing.
    This implementation uses a fixed-size hash table based on the ASCII character set (1–256).  
    Each character in the input strings is converted to its ASCII code, and the corresponding index 
    in the hash table is incremented to track frequency.
    Repeated characters increase the count at their respective ASCII index.

    The class provides a method to retrieve the frequency of any character based on this hash mapping.
    """
    def __init__(self, array: list[str]):
        self.str_array = array
        self._create_hash()
        self._pre_process_hash()

    def _create_hash(self):
        """
        Create a hash table using dictionary from the array size.
        """
        self.hash_str_array = [0] * 256 # Considering all ASCII characters
        
    def _pre_process_hash(self):
        """
        Preload the hash table with the number of times each string appears in the array.
        """
        for char in self.str_array:
            self.hash_str_array[ord(char)] += 1

    def find_count(self, char: str) -> str:
        """
        Find the number of times a string appears in the array.
        """
        return self.hash_str_array[ord(char)]
    
    def find_max_min_frequencies(self) -> tuple:
        """
        Find the maximum and minimum frequencies of characters in the hash table.
        """
        max_freq = max(self.hash_str_array)
        max_chars = [chr(i) for i, freq in enumerate(self.hash_str_array) if freq == max_freq]
        # Replace 0 with 999 to avoid confusion with min frequency
        for i in self.hash_str_array:
            if i == 0:
                self.hash_str_array[self.hash_str_array.index(i)] = 999
        min_freq = min(self.hash_str_array)
        min_chars = [chr(i) for i, freq in enumerate(self.hash_str_array) if freq == min_freq]
        return (max_chars, min_chars)
    

from collections import Counter

class HashfindStrCounter:
    """_summary_
        Counter implementation of the same string hashing above
        """
    def __init__(self, array: list[str]):
        self.str_array = array
        self.hash_counter = Counter(self.str_array)

    def find_count(self, char: str) -> str:
        """
        Find the number of times a string appears in the array.
        """
        return self.hash_counter[char]


if __name__ == "__main__":
    input_array = input("Enter the array of characters split by comma: ")
    char_array = [char for char in input_array.split(',')]

    hash_finder = HashFindStr(char_array)
    # hash_finder = HashfindStrCounter(char_array)
    
    while(True):
        char_to_count = input("Enter the char to find its count: ")
        if char_to_count == '.':
            max, min = hash_finder.find_max_min_frequencies()
            print(f"Max Frequecy char -> {max} and Min Frequency char -> {min}")
            break
        else:
            print(f"The Number {char_to_count} appears {hash_finder.find_count(char_to_count)} times")
        