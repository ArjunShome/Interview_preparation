# def spiralTraverse(array):
#     # Write your code here.
#     traversed_list = []
#     top = 0
#     right = len(array[0]) - 1
#     bottom = len(array) - 1
#     left = 0
#     if len(array) == 1:
#         return array[0]

#     while top <= bottom and left <= right:
#         for idx in range(left, right + 1):
#             traversed_list.append(array[top][idx])
#         top += 1

#         for idx in range(top, bottom + 1):
#             traversed_list.append(array[idx][right])
#         right -= 1

#         for idx in range(right, left - 1, - 1):
#             traversed_list.append(array[bottom][idx])
#         bottom -= 1

#         for idx in range(bottom, top - 1, - 1):
#             traversed_list.append(array[idx][left])
#         left += 1
#     return traversed_list


def spiralTraverse(array):
    # Write your code here.
    top  = 0
    bottom = len(array) - 1
    left = 0
    right = len(array[0]) - 1
    lst_numbers = []

    if len(array) == 1:
        return array[0]

    while top <= bottom and left <= right:
        for idx in range(left, right + 1):
            lst_numbers.append(array[top][idx])
        top += 1

        for idx in range(top, bottom + 1):
            lst_numbers.append(array[idx][right])
        right -= 1
        
        if top <= bottom:
            for idx in range(right, left - 1, - 1):
                lst_numbers.append(array[bottom][idx])
            bottom -= 1
        
        if left <= right:
            for idx in range(bottom, top - 1, -1):
                lst_numbers.append(array[idx][left])
            left += 1

    return lst_numbers

if __name__ == '__main__':
    array = [
        [1,2,3,4],
        [12,13,14,5],
        [11,16,15,6],
        [10,9,8,7]
    ]
#     array = [
#         [1,2,3],
#         [8,9,4],
#         [7,6,5]
#     ]

#     array = [
#     [1, 2, 3, 4],
#     [10,11,12,5],
#     [9, 8, 7, 6]
#   ]
    array= [
        [1, 2, 3],
        [12, 13, 4],
        [11, 14, 5],
        [10, 15, 6],
        [9, 8, 7]
    ]

    print(spiralTraverse(array))