def moveElementToEnd(array, toMove):
    # Write your code here.
    end = len(array) - 1
    start = 0
    while start <= end: 
        if array[end] == toMove:
            end -= 1
            continue
        if array[start] == toMove:
            array[start], array[end] = array[end], array[start]
            end -= 1
        start += 1
    return array

if __name__ == '__main__':
    array = [2,1,2,2,2,3,4,2]
    toMove = 2
    print(moveElementToEnd(array, toMove))