
class LongestSumArray:
    def __init__(self, array, key):
        self.arr = array
        self.key = key

    def longest_subarray_sum_brute(self):
        longest_len = 0
        for i in range(len(self.arr)-1):
            sum = 0
            for j in range(i, len(self.arr)-1):
                sum += arr[j]
                if sum == self.key:
                    longest_len = max(longest_len, j - i + 1)
        return longest_len
    
    def longest_subarray_sum_hashing(self):
        # Best for both positive and negative numbers
        max_len = 0
        sum = 0
        presum_map = {}

        for i in range(len(self.arr)-1):
            sum += self.arr[i]

            if sum == self.key:
                max_len = max(max_len, i + 1)
            
            rem = sum - self.key
            if rem in presum_map.keys():
                max_len = max(max_len, i - presum_map[rem])

            if sum not in presum_map.keys():
                presum_map[sum] = i

        return max_len
    

    def longest_subarray_sum_optimized(self):
        # Optimized Just for positive and Zeros
        i = 0
        j = 0
        sum = 0
        max_len = 0

        while j < len(self.arr) - 1:
            sum += self.arr[j]
            
            if sum > self.key:
                sum -= self.arr[i]
                i+=1

            if sum == self.key:
                max_len = max(max_len, (j - i) + 1)
            
            j+=1
        return max_len

            


if __name__ == '__main__':
    input_arr = input("Enter the array of numbers seperated by comma: ")
    arr = [int(el) for el in input_arr.split(",")]
    ll = LongestSumArray(arr, 6)
    print(ll.longest_subarray_sum_brute())
    print(ll.longest_subarray_sum_hashing())
    print(ll.longest_subarray_sum_optimized())
