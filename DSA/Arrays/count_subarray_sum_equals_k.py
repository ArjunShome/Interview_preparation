
class SubarraySum:
    def __init__(self, array, k):
        self.arr = array
        self.key = k

    def count_subarray_sum_k(self):
        presum_map = 0
        hash = {}
        count = 0

        for i in range(len(self.arr)):
            if presum_map == 0:
                hash[presum_map] = 1 
            
            presum_map += self.arr[i]
            rem = presum_map - self.key

            if rem in hash:
                if rem == 0:
                    if presum_map in hash:
                        count += hash[presum_map]
                    else:
                        count += 1
                else:
                    count += hash[rem]
            
            if presum_map in hash:
                hash[presum_map] += 1
            else:
                hash[presum_map] = 1
                
        return count


if __name__ == '__main__':
    input_arr = input("Enter the array of numbers separated by comma: ")
    input_arr = [int(num) for num in input_arr.split(",")]
    inp_key = int(input("Enter the number to check for the sum: "))
    sa = SubarraySum(input_arr, inp_key)
    print(sa.count_subarray_sum_k())
