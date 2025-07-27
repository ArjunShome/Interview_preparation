
def levenshteinDistance(str1, str2, i = None, j = None, memo = None):
    # Write your code here.
    if i is None:
        i = len(str1) - 1
    if j is None:
        j = len(str2) - 1
        
    if memo is None:
        memo = {}
    if  i < 0:
       return j + 1

    if j < 0:
        return i + 1

    if (i,j) in memo:
        return memo[(i,j)]
        
    if str1[i] == str2[j]:
        return 0 + levenshteinDistance(str1, str2, i - 1, j - 1, memo)
    else:
        steps_ins = 1 + levenshteinDistance(str1, str2, i, j - 1, memo)  # Insert
        steps_del = 1 + levenshteinDistance(str1, str2, i - 1, j, memo)  # Delete
        steps_rep = 1 + levenshteinDistance(str1, str2, i - 1, j - 1, memo)  # Replace

    memo[(i,j)] = min(steps_ins, steps_del, steps_rep)
    return  memo[(i,j)]

if __name__ == '__main__':
    str1 = "abc"
    str2 = "yabd"
    print(levenshteinDistance(str1, str2))