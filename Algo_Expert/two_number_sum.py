

def twoNumberSum(array, targetSum):
    # Write your code here.
    hash_table = {}
    for i in range(len(array)): 
        num = targetSum - array[i]
        if num not in hash_table:
            hash_table[array[i]]=1
        else:
            return [array[i], num]
    return []


if __name__ == "__main__":
    array = [4,6]
    targetSum = 10
    print(twoNumberSum(array=array, targetSum=targetSum))