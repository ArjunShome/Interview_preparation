
def longestPalindromicSubstring(string):
    # Write your code here.
    longest_palindrome = ""
    count = 0

    for i in range(len(string)):
        # Even case check  
        if (i - 1) >= 0 and string[i] == string[i - 1]:
            longest_palindrome = string[i-1 : i + 1] if len(string[i-1 : i + 1]) > len(longest_palindrome) else longest_palindrome
            left = i - 2
            right = i + 1
            while left >= 0 and right <= len(string)-1:       
                if string[left] == string[right]:
                    cur_str = string[left : right + 1]
                    longest_palindrome = cur_str if len(cur_str) > len(longest_palindrome) else longest_palindrome
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
        # Odd Case Check
        if (i - 1) >= 0 and i != len(string) - 1 and string[i + 1] == string[i - 1]:
            longest_palindrome = string[i-1 : i + 2] if len(string[i-1 : i + 2]) > len(longest_palindrome) else longest_palindrome
            left = i - 2
            right = i + 2
            while left >= 0 and right <= len(string)-1:       
                if string[left] == string[right]:
                    cur_str = string[left : right + 1]
                    longest_palindrome = cur_str if len(cur_str) > len(longest_palindrome) else longest_palindrome
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
        longest_palindrome = string[i] if len(longest_palindrome) == 0 else longest_palindrome
    return longest_palindrome, count + 1

    


if __name__ == "__main__":
    string = "abaxyzzyxf"
    string = "abcdefghfedcbaa"
    string = "abcdefgfedcba"
    string = "aca"
    print(longestPalindromicSubstring(string))