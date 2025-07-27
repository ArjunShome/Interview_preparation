
# def numberOfWaysToMakeChange(n, denoms, index=0, lst_ways=None):
#     # Write your code here.
#     if index == n:
#         return lst_ways
        
#     if lst_ways is None:
#         lst_ways = [0] * (n + 1)
#         lst_ways[0] = 1 

#     for denom in denoms:
#         if index >= denom:
#             lst_ways[index] += lst_ways[index - denom]
#         numberOfWaysToMakeChange(n, denoms, index + 1, lst_ways)
#     return lst_ways


def numberOfWaysToMakeChange(n, denoms, index=0, lst_ways=None):
    # Write your code here.        
    if lst_ways is None:
        lst_ways = [0] * (n + 1)
        lst_ways[0] = 1

    for denom in denoms:
        for i in range(1, len(lst_ways)):
            if i >= denom:
                lst_ways[i] += lst_ways[i - denom]
    return lst_ways[n]

if __name__ == '__main__':
    denoms = [5,1]
    number = 6
    print(numberOfWaysToMakeChange(number, denoms))
