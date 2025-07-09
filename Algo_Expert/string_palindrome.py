def isPalindrome(string):
    # Write your code here.
    left = 0
    right = len(string) - 1
    while left <= right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

    # actual_lst = list(string)
    # reversed_lst = []
    # for i in range(len(actual_lst), 0, -1):
    #     reversed_lst.append(actual_lst[i - 1])
    # if actual_lst == reversed_lst:
    #     return True
    # else:
    #     return False


if __name__ == '__main__':
    string = "abcdcba"
    print(isPalindrome(string))