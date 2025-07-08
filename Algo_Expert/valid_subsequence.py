def isValidSubsequence(array, sequence):
    # Write your code here.
    j = 0
    i = 0
    if len(sequence) > len(array):
            return False
    while i <= len(array)-1:
        if sequence[j] == array[i]:
            j += 1
            i += 1
        else:
            i+=1
        if j == len(sequence):
            return True
    return False
            


if __name__ == "__main__":
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(isValidSubsequence(array=array, sequence=sequence))