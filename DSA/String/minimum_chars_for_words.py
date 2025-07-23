def minimumCharactersForWords(words):
    # Write your code here.
    final_lst = []
    final_dict = {}
    for word in words:
        cur_dict = {}
        for char in word:
            if char not in cur_dict:
                cur_dict[char] = 1
            else:
                cur_dict[char] += 1
        for char in cur_dict:
            if char in final_dict:
                final_dict[char] = max(cur_dict[char], final_dict[char])
            else:
                final_dict[char] = cur_dict[char]
    for key, value in final_dict.items():
        final_lst.extend([key] * value)
    return final_lst

if __name__ == '__main__':
    list_words = ["this", "that", "did", "deed", "them!", "a"]
    print(minimumCharactersForWords(list_words))