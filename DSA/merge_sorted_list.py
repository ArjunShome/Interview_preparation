


class Solution:
    @staticmethod
    def merge(nums1, m, nums2, n):
        j = n-1
        k = m + n - 1
        i = m - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                nums1[i] = nums2[j]
                k -=1
                i -=1
            else:
                nums1[k] = nums2[j]
                k -=1
                j -=1
        return nums1


        

    

if __name__ == '__main__':
    nums1 = [2,0]
    nums2 = [1]
    m = 1
    n = 1
    print(Solution.merge(nums1, m, nums2, n))
