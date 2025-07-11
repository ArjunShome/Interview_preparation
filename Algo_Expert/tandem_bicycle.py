

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    i = 0
    j = 0
    total_speed = 0

    if fastest:
        redShirtSpeeds.sort(reverse=True)
        blueShirtSpeeds.sort()
    else:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()
        
    while i <= len(redShirtSpeeds) - 1 and j <= len(blueShirtSpeeds) - 1:
        total_speed += max(redShirtSpeeds[i], blueShirtSpeeds[j])
        i += 1
        j += 1

    return total_speed


if __name__ == '__main__':
    redShirtSpeeds = [5, 5, 3, 9, 2]
    blueShirtSpeeds = [3, 6, 7, 2, 1]
    fastest = True
    print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest))