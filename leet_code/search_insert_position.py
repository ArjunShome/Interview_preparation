
class Solution:
    @staticmethod
    def searchInsert(nums, target) -> int:
        low = 0
        high = len(nums) - 1
        indx = -1
        while low <= high:
            mid = int(low + (high - low)/2)
            if nums[mid] >= target:
                indx = mid
                high = mid - 1
            else:
                low = mid + 1
            if low > high and high == (len(nums) - 1):
                return len(nums)
        return indx




if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 7
    print(Solution.searchInsert(nums, target))