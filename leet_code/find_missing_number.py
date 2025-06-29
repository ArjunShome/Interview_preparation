
class Solution:
    @staticmethod
    def missingNumbers(nums) -> int:
        expected_xor = 0 
        actual_xor = 0
        for num in range(len(nums)+1):
            expected_xor ^= num

        for num in nums:
            actual_xor ^= num
        
        return actual_xor ^ expected_xor


if __name__ == '__main__':
    arr = [9,6,4,2,3,5,7,0,1]
    # output = 0
    print(Solution.missingNumbers(arr))
