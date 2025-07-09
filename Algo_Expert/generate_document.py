def generateDocument(characters, document):
    # Write your code here.
    seen_chars = {}
    
    for ch in characters:
        if ch not in seen_chars:
            seen_chars[ch] = 1
        else:
            seen_chars[ch] += 1

    for char in document:
        if char not in seen_chars:
            return False
        if seen_chars[char] == 0:
            return False
        seen_chars[char] -= 1

    return True


if __name__ == '__main__':
    characters = "Bste!hetsi ogEAxpelrt x "
    document = "AlgoExpert is the Best!"
    print(generateDocument(characters, document))
