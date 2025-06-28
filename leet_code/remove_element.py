
class Solution:
    @staticmethod
    def removeElement(nums, val) -> int:
        i = 0
        j = len(nums)- 1
        count = 0
        while i <= j:
            if nums[j] == val:
                j -=1
                count += 1
            elif nums[i] == val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j -= 1
                i += 1
                count += 1
            else:
                i +=1
        return len(nums) - count





if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    k = Solution.removeElement(nums, val)
    print(k)