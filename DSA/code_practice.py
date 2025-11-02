"""
✅ Question 1 – Easy (Stack + String Logic)

🧩 Valid Parentheses — (LeetCode #20, Easy)

Given a string containing just the characters (), {}, [], determine if the input string is valid.

✅ A string is valid if:
	•	Open brackets must be closed by the same type of brackets.
	•	Open brackets must be closed in the correct order.
	•	An empty string is considered valid.

Examples
Input         Output
"()"            True
"()[]{}"        True
"(]"            False
"([)]"          False
"{"             False


✅ Question 2 – Medium (Binary Search + Lists)

🎯 Search Insert Position — (LeetCode #35, Easy/Medium Level Logic)

Given a sorted list of integers and a target, return the index if the target is found. If not, return the index where it would be inserted to maintain order.

You must write an algorithm with O(log n) complexity (binary search logic).

Examples

Input                                       Output
nums = [1, 3, 5, 6], target = 5                2
nums = [1, 3, 5, 6], target = 2                1
nums = [1, 3, 5, 6], target = 7                4
nums = [1, 3, 5, 6], target = 0                0


"""

# Solution 2
def search_insert_position(lst_nums: list, target: int) -> int:
    left = 0
    right = len(lst_nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if lst_nums[mid] == target:
            return mid
        if lst_nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


# Solution 1
def valid_parantheses(input: str) -> bool:
    stack = []
    for ch in input:
        if ch in "({[":
            stack.append(ch)

        elif ch == ")" and len(stack) > 0 and stack[-1] == "(":
            stack.pop()
        elif ch == "]" and len(stack) > 0 and stack[-1] == "[":
            stack.pop()
        elif ch == "}" and len(stack) > 0  and stack[-1] == "{":
            stack.pop()
        else:
            return False

    return len(stack) == 0



if __name__=='__main__':
    input = "()"
    if valid_parantheses(input):
        print("Valid Parentheses provided")
    else:
        print("InValid Parentheses provided")

    lst = [1, 3, 5, 6]
    target = 2
    print(search_insert_position(lst, target))
