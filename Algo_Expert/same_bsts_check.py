
def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
    if len(arrayOne) != len(arrayTwo):
        return False
    if arrayOne[0] != arrayTwo[0]:
        return False

    left_subtree_array_one = get_left_subtree(arrayOne, arrayOne[0])
    right_subtree_array_one = get_right_subtree(arrayOne, arrayOne[0])
    left_subtree_array_two = get_left_subtree(arrayTwo, arrayTwo[0])
    right_subtree_array_two = get_right_subtree(arrayTwo, arrayTwo[0])

    
    is_left_subtree = sameBsts(left_subtree_array_one, left_subtree_array_two)
    is_right_subtree = sameBsts(right_subtree_array_one, right_subtree_array_two)

    return is_left_subtree and is_right_subtree

def get_left_subtree(array, root):
    subtree = []
    for el in array:
        if el < root:
            subtree.append(el)
    return subtree

def get_right_subtree(array, root):
    subtree = []
    if len(array) == 1:
        return subtree
    for i in range(len(array)):
        if array[i] >= root and i != 0:
            subtree.append(array[i])
    return subtree

if __name__ == '__main__':
    # arrayOne = [10,15,8,12,94,81,5,2,11]
    # arrayTwo = [10,8,5,15,2,12,11,94,81]

    arrayOne = [5, 2, -1, 100, 45, 12, 8, -1, 8, 10, 15, 8, 12, 94, 81, 2, -34]
    arrayTwo = [5, 8, 10, 15, 2, 8, 12, 45, 100, 2, 12, 94, 81, -1, -1, -34, 8]

    print(sameBsts(arrayOne, arrayTwo))
