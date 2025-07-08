
class FindInSortedArrayDups:
    def __init__(self, array, target):
        self.array = array
        self.target = target

    def find(self):
        left = 0
        right = len(self.array) - 1

        while left <= right:
            mid = left + (right - left)//2
            if self.array[mid] == self.target:
                return mid
            # if duplicates then reduce low and increase high by 1
            if self.array[mid] == self.array[left] and self.array[right] == self.array[mid]:
                left += 1
                right -= 1
                continue
            
            elif self.array[left] <= self.array[mid]:
                if target >= self.array[left] and target <= self.array[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= self.array[right] and target >= self.array[mid]:
                    left = mid + 1
                else:
                    right = mid - 1



# duplicates
if __name__ == '__main__':
    arr = [7,8,1,2,3,3,3,4,5,6] 
    target = 6
    fn = FindInSortedArrayDups(arr, target)
    print(fn.find())