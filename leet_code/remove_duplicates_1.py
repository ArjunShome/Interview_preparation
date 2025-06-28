
class Solution:
    @staticmethod
    def removeduplicates(nums) -> int:
        i = 0
        j = 1
        rem_val = -101
        dups = 0
        while j < len(nums):
            if nums[i] == nums[j]:
                rem_val = nums[j]
                j += 1
                dups += 1
            else:
                nums[i+1] = nums[j]
                i += 1
                j += 1
        return len(nums) - dups


if __name__ == '__main__':
    nums = [1,1,2]
    print(Solution.removeduplicates(nums))
