


def zeroSumSubarray(nums):
    # Write your code here.
    seen = set()
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum == 0 or current_sum in seen:
            return True
        else:
            seen.add(current_sum)
    return False


if __name__ == '__main__':
    nums = [-5, -5, 2, 3, -2]
    # nums = [1, 2, -2, 3]
    # nums = [2 ,  -2]
    print(zeroSumSubarray(nums))