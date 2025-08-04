
def sweetAndSavory(dishes, target):
    # Write your code here.
    left = 0
    right = len(dishes) - 1
    best_match = float('inf')
    best_dish = [0, 0]
    dishes.sort()

    while left < right:
        if len(dishes) > 1:
            if dishes[left] > 0 or dishes[right] < 0:
                break
            potential_match = dishes[left] + dishes[right]
            if potential_match > target:
                right -= 1
            elif potential_match == target:
                return [dishes[left], dishes[right]]
            else:
                if target - potential_match <= best_match:
                    best_match = target - potential_match
                    best_dish = [dishes[left], dishes[right]]
                left += 1
    return best_dish

if __name__ == '__main__':
    # array = [5, 2, -7, 30, 12, -4, -20]
    #       [-20, -7, -4, 2, 5, 12, 30]
    # array = [-5, 10]
    # array = [5,-5,5,-5,5,-5]
    # array = [-3, -5, 1, 7] # [-5,-3,1,7]
    array = [2, 5, -4, -7, 12, 100, -25]
    target = 7
    print(sweetAndSavory(array, target))
    