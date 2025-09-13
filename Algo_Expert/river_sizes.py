def riverSizes(matrix):
    sizes = []
    seen = [[False for _ in range(len(matrix[0]))] for row in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if seen[i][j]:
                continue
            traverseCheck(i, j, matrix, seen, sizes)
    return sizes

def traverseCheck(i, j, matrix, seen, sizes):
    countRiverSize = 0
    neighboursToProcess = [[i, j]]

    while len(neighboursToProcess):
        currentNode = neighboursToProcess.pop()
        i = currentNode[0]
        j = currentNode[1]

        if seen[i][j]:
            continue
        
        seen[i][j] = True

        if matrix[i][j] == 0:
            continue

        countRiverSize += 1

        neighbours = getNeighbours(i, j, matrix, seen)

        for neighbour in neighbours:
            neighboursToProcess.append(neighbour)

    if countRiverSize > 0:
        sizes.append(countRiverSize)


def getNeighbours(i, j, matrix, seen):
    neighbours = []

    if i > 0 and not seen[i - 1][j]:
        neighbours.append([i - 1, j])
    if i < len(matrix) - 1 and not seen[i + 1][j]:
        neighbours.append([i + 1, j])
    if j > 0 and not seen[i][j - 1]:
        neighbours.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not seen[i][j + 1]:
        neighbours.append([i, j + 1])
    
    return neighbours

if __name__ == '__main__':
    matrix = [
        [1,0,0,1,0],
        [1,0,1,0,0],
        [0,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,1,0]
    ]

    print(riverSizes(matrix))