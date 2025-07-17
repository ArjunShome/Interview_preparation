
def balancedBrackets(string):
    # Write your code here.
    balanced_bracket_list = []
    head = None
    bracket_map = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    for char in string:
        if char in bracket_map or char in bracket_map.values():
            if char in bracket_map.values():
                balanced_bracket_list.append(char)
                head = char
            else:
                if bracket_map[char] != head or len(balanced_bracket_list) == 0:
                    return False
                head = balanced_bracket_list[-2] if len(balanced_bracket_list) >= 2 else None
                balanced_bracket_list.pop()
    return True if head is None else False

if __name__ == '__main__':
    string = "{[[[[({(}))]]]]}"
    print(balancedBrackets(string))