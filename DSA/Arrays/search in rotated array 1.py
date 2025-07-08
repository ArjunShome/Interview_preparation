
class FindInRotatedArray:
    def __init__(self, array, target):
        self.array = array
        self.target = target

    def find(self):
        left = 0
        right = len(self.array) - 1

        while left <= right:
            mid = left + (right - left)//2
            # return if match
            if self.array[mid] == target:
                return mid
            # check if left sorted else the right sorted
            if self.array[left] <= self.array[mid]: 
                # check if target inside left and mid else inside mid and right
                if target >= self.array[left] and target <= self.array[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= self.array[right] and target >= self.array[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# unique
if __name__ == '__main__':
    arr = [7,8,1,2,3,4,5,6]
    target = 2
    fra = FindInRotatedArray(arr, target)
    print(fra.find())