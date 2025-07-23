def oneEdit(stringOne, stringTwo):
    # Write your code here.
    diff = 0
    if abs(len(stringOne) - len(stringTwo)) > 1:
        return False
    
    if len(stringOne) != len(stringTwo):
        bigger_string = stringOne if len(stringOne) > len(stringTwo) else stringTwo
        smaller_string = stringOne if len(stringOne) < len(stringTwo) else stringTwo
        i = j = 0
        diff = 0
        while i < len(smaller_string) and j < len(bigger_string):
            if smaller_string[i] != bigger_string[j]:
                if diff == 1:
                    return False
                diff += 1
                j += 1  # skip one char in longer string
            else:
                i += 1
                j += 1

    else:
        for i in range(len(stringTwo)):
            if stringOne[i] != stringTwo[i]:
                diff += 1
            if diff > 1:
                return False
    return True

if __name__ == '__main__':
    stringOne = "hello"
    stringTwo = "helo"
    print(oneEdit(stringOne, stringTwo))

