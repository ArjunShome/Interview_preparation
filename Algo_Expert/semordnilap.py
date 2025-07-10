def semordnilap(words):
    # Write your code here.
    word_set = set(words)
    seen = set()
    word_pairs = []
    for word in words:
        reversed_word = "".join(list(word)[::-1])
        if reversed_word in word_set and reversed_word not in seen and reversed_word != word:
            seen.add(word)
            seen.add(reversed_word)
            word_pairs.append([word, reversed_word]) 
    return word_pairs


if __name__ == '__main__':
    words = ["aaa", "bbbb"]
    print(semordnilap(words=words))