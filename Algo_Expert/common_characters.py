
def commonCharacters(strings):
    # Write your code here.
    seen = {}
    common_chars = []
    if len(strings) == 1:
        return strings
    for string in strings:
        for char in set(string):
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1
    for char in seen:
        if seen[char] >= len(strings):
            common_chars.append(char)
    return common_chars


if __name__ == '__main__':
    strings = ["abcde", "aa", "foobar", "foobaz", "and this is a string", "aaaaaaaa", "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeea"]
    print(commonCharacters(strings))