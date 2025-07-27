

# def minNumberOfCoinsForChange(number, denoms, count=0):
#     if number == 0:
#         return 0
#     if number < 0:
#          return float('inf')
    
#     min_count = float('inf')
#     for denom in denoms:
#         count = minNumberOfCoinsForChange(number - denom, denoms)
#         if count != float('inf'):
#             min_count = min(min_count, count + 1)
#     return min_count


def minNumberOfCoinsForChange(number, denoms, index=0):
    if number == 0:
        return 0
    if not any(number % denom == 0 for denom in denoms):
        return -1
    
    lst_amt = [float('inf')] * (number + 1)
    lst_amt[0] = 0

    for denom in denoms:
        for amount in range(1, len(lst_amt)):
            if amount >= denom:
                lst_amt[amount] = min(lst_amt[amount], lst_amt[amount - denom] + 1)
    return lst_amt[number]

if __name__ == '__main__':
    number = 7
    denoms = [1,5]
    print(minNumberOfCoinsForChange(number, denoms))
