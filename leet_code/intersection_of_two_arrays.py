

class Solution:
    @staticmethod
    def intersection(array1, array2):
        array1 = sorted(array1)
        array2 = sorted(array2)
        seen = set()
        i = 0
        j = 0
        while i < len(array1) and j < len(array2):
            if array1[i] == array2[j]:
                seen.add(array1[i])
                j+=1
                i+=1
            elif array1[i] < array2[j]:
                i+=1
            else:
                j+= 1
        return seen

if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(Solution.intersection(nums1, nums2))