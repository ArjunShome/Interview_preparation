
def sweetAndSavory(dishes, target):
    # Write your code here.
    sweet_dishes = []
    savory_dishes = []

    for el in dishes:
        if el < 0:
            sweet_dishes.append(el)
        else:
            savory_dishes.append(el)

    sweet_dishes.sort(reverse=True)
    savory_dishes.sort()

    i = 0
    j = 0
    balanced_dish = []
    balanced_dish_sum = 0
    balanced_dish_dif_from_target = 0
    while i <= len(sweet_dishes) - 1 or j <= len(savory_dishes) - 1:
        if len(balanced_dish) == 0:
           balanced_dish.append(sweet_dishes[0])
           balanced_dish.append(savory_dishes[0])
           balanced_dish_sum = balanced_dish[0] + balanced_dish[1] 
           balanced_dish_dif_from_target = target - balanced_dish_sum 
           i += 1
           j += 1
           continue

        new_dish = sweet_dishes[i] + savory_dishes[j]
        if (target - new_dish) < balanced_dish_dif_from_target:
            balanced_dish[0] = sweet_dishes[i]
            balanced_dish[1] = savory_dishes[j]
            balanced_dish_sum = new_dish
            balanced_dish_dif_from_target = target - balanced_dish_sum 
        else:
            if new_dish > target:
                i += 1
            else:
                j += 1
            continue
        if balanced_dish_sum < target:
            j += 1
        elif balanced_dish_sum > target:
            i += 1

    return balanced_dish


if __name__ == '__main__':
    array = [5, 2, -7, 30, 12, -4, -20]
    target = 4
    print(sweetAndSavory(array, target))
    