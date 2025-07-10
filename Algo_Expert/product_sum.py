
# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, level = 1):
    # Write your code here.
    count = 0
    for el in array:
        if isinstance(el, int):
            count += el
        elif isinstance(el, list):
            count += productSum(el, level + 1)
    return count * level


if __name__ == '__main__':
    array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    print(productSum(array, 1))