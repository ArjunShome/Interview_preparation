
class MinimumInRotatedSortedArray:
    def __init__(self, array):
        self.array = array

    def get_minimum(self):
        left = 0
        right = len(self.array) - 1
        number_idx = (right, right)

        while left <= right:
            mid = left + (right - left) // 2

            # left sorted
            if self.array[mid] >= self.array[left]:
                if number_idx[0] > self.array[left]:
                    number_idx = (self.array[left], left)
                left = mid + 1
            # right sorted
            else:
                if number_idx[0] > self.array[mid]:
                    number_idx = (self.array[mid], mid)
                right = mid - 1
        return number_idx[1]


if __name__ == '__main__':
    array = [3,4,5,1,2]
    mirs = MinimumInRotatedSortedArray(array)
    print(mirs.get_minimum())
