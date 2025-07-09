

def firstNonRepeatingCharacter(string):
    # Write your code here.
    seen = {}
    for idx in range(len(string)):
        if string[idx] not in seen:
            seen[string[idx]] = [idx, 1]
        else:
            seen[string[idx]][1] += 1

    for char in seen:
        if seen[char][1] == 1:
            return seen[char][0]

    return -1


if __name__ == '__main__':
    string = "faadabcbbebdf"
    print(firstNonRepeatingCharacter(string))