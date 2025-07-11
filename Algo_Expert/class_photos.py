


def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    i = 0
    j = 0
    possible = False
    if redShirtHeights[0] < blueShirtHeights[0]:
        while i <= len(redShirtHeights) - 1 and j <= len(blueShirtHeights) - 1:
            if redShirtHeights[i] < blueShirtHeights[j]:
                possible = True
                i += 1
                j += 1
            else:
                possible = False
                break
    else:
        while i <= len(redShirtHeights) - 1 and j <= len(blueShirtHeights) - 1:
            if redShirtHeights[i] > blueShirtHeights[j]:
                possible = True
                i += 1
                j += 1
            else:
                possible = False
                break

    return possible


if __name__ == '__main__':
    redShirtHeights =  [5, 8, 1, 3, 4]
    blueShirtHeights = [6, 9, 2, 4, 5]
    print(classPhotos(redShirtHeights, blueShirtHeights))
