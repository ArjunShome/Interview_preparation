
# Check for a palindrome string
# ABA -> Palindrome Number
# ABB -> Not a Palindrome Number

def check_palindrome(count, check_str: list):
    if count >= len(check_str)/2:
        return True
    if check_str[count] != check_str[len(check_str)-count-1]:
        return False
    return check_palindrome(count+1, check_str)



if __name__ == "__main__":
    check_str = input("Enter the String do PAlindrome Check: ")
    check_str = [char for char in check_str.split(",")]
    count = 0
    result = check_palindrome(count, check_str)
    print("The Input is a Palindrome String" if result else "Non Palindrome")