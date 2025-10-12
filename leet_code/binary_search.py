import time
from line_profiler import profile

def binary_search(arr: list[int], key: int) -> bool:
    arr.sort()
    exists = False
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            exists = True
            break
        if key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return exists

@profile
def binary_search_rec(arr: list[int], key: int) -> bool:
    arr.sort()
    left = 0
    right = len(arr) - 1
    mid = left + (right - left) // 2
    exist = helper(arr, key, mid, left, right)
    time.sleep(3)
    return exist

@profile
def helper(arr, key, mid, left, right):
    if arr[mid] == key:
        return True
    if left > right:
        return False
    if key < arr[mid]:
        right = mid - 1
    else:
        left = mid + 1
    mid = left + (right - left) // 2
    return helper(arr, key, mid, left, right)

if __name__ == '__main__':
    print(binary_search([1,6,4,3,9,28,7], 9))
    print(binary_search_rec([1, 6, 4, 3, 9, 28, 7], 1))

    # lp = LineProfiler()
    # lp.add_function(helper)
    # lp_wrapper = lp(binary_search_rec)
    # lp_wrapper()
    # lp.print_stats(output_unit=1e-03)