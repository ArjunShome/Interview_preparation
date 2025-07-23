def reverseWordsInString(string):
    # Write your code here.
    lst_words = mySplit(string)
    final_str = ""
    for i in range(len(lst_words) - 1, -1, -1):
        if i == 0 :
            final_str = final_str + lst_words[i]
            return final_str
        final_str = final_str + lst_words[i] + " "

def mySplit(string, split_on = " "):
    lst_words = []
    cur_str = ""
    for i in range(len(string)):
        if string[i] != " ":
            cur_str += string[i]
        else:
            lst_words.append(cur_str)
            cur_str = ""
    lst_words.append(cur_str)
    return lst_words

if __name__ == '__main__':
    string = "Algoexpert is the best!"
    print(reverseWordsInString(string))
