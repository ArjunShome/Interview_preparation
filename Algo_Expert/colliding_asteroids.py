def collidingAsteroids(asteroids):
    # Write your code here.
    stack = []
    for current_asteroid in asteroids:
        while stack and stack[-1] > 0 and current_asteroid < 0:
            if abs(current_asteroid) > stack[-1] and stack[-1] > 0:
                stack.pop()
            elif stack[-1] + current_asteroid == 0:
                stack.pop()
                break
            elif stack[-1] > current_asteroid:
                break
            # Same asteroid at same direction
            else:
                stack.append()
        else:
            stack.append(current_asteroid)
    return stack


if __name__ == '__main__':
    asteroids = [-3, 5, -8, 6, 7, -4, -7]
    asteroids = [1, 2, 3, -4]
    # asteroids = [-70, 100, 23, 42, -50, -75, 1, -2, -3]
    print(collidingAsteroids(asteroids))
