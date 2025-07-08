
class MinimumInRotatedSortedArray:
    def __init__(self, array):
        self.array = array

    def get_minimum(self):
        left = 0
        right = len(self.array) - 1
        number = max(self.array)

        while left <= right:
            mid = left + (right - left) // 2

            # left sorted
            if self.array[mid] >= self.array[left]:
                number = min(number, self.array[left])
                left = mid + 1
            # right sorted
            else:
                number = min(number, self.array[mid])
                right = mid - 1
        return number


if __name__ == '__main__':
    array = [7,8,1,2,3,4,5,6]
    mirs = MinimumInRotatedSortedArray(array)
    print(mirs.get_minimum())

