
def blackjackProbability(target, startingHand, memo = {}):
    if startingHand in memo:
        return memo[startingHand]
    
    # Write your code here.
    if startingHand >= (target - 4) and startingHand < target:
        return 0
    if startingHand >= target:
        return 1
    
    total_bust_prob = 0
    for i in range(1, 10):
        total_bust_prob += 0.1 * blackjackProbability(target, startingHand + i)
    memo[startingHand] = round(total_bust_prob, 2)
    return round(total_bust_prob, 2)

if __name__ == '__main__':
    target = 21
    startingHand = 14


    print(blackjackProbability(target, startingHand))
