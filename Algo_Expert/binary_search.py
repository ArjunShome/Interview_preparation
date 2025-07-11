
def binarySearch(array, target):
    # Write your code here.
    left = 0
    right = len(array)- 1

    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return -1



if __name__ == '__main__':
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33
    print(binarySearch(array, target))