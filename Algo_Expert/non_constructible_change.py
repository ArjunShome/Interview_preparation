

def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    change = 0

    for i in range(len(coins)):
        if coins[i] <= change + 1:
            change += coins[i]
    return change + 1


if __name__ == '__main__':
    coins = [1, 1, 1, 1, 1]
    print(nonConstructibleChange(coins=coins))