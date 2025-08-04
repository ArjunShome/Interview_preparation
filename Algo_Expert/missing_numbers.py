def missingNumbers(nums):
    # Write your code here.
    if len(nums) == 0:
        return []
    nums.sort()
    max_num = len(nums) + 2
    min_num = min(nums)
    missing_nums = []
    for i in range(min_num, max_num + 1):
        if i not in nums:
            missing_nums.append(i)
    return missing_nums


if __name__ == '__main__':
    nums = [1, 4, 3]
    print(missingNumbers(nums))