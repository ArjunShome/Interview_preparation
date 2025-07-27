def getPermutations(array):
    # Write your code here.
    if not array:
        return []
    final_lst = []
    recurse_perm(array, final_lst, index = 0)
    return final_lst

def recurse_perm(array, final_array, index):
    if index == len(array):
        cur_Array = array.copy()
        final_array.append(cur_Array)
    
    for i in range(index, len(array)):
        swap(i, index, array)
        recurse_perm(array, final_array, index + 1)
        swap(i, index, array)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    array = [1,2,3]
    print(getPermutations(array))
