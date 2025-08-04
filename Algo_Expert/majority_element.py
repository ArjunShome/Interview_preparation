def majorityElement(array):
    # Write your code here.
    num = None
    seen = 0

    for el in array:
        if num == el and seen > 0:
            seen += 1
        elif seen == 0:
            num = el
            seen = 1
        else:
            seen -= 1
    if seen > 0:
        return num
    return -1

if __name__ == '__main__':
    array = [1,2,3,2,2,1,2]
    array = [2]
    print(majorityElement(array))