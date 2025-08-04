
def searchInSortedMatrix(matrix, target):
    # Write your code here.
    i = 0
    while i <= len(matrix) - 1:
        j = 0
        while j <= len(matrix):
            if matrix[i][j] == target:
                return [i, j]
            elif matrix[i][j] < target:
                j += 1
            else:
                break
                
        i += 1
    return [-1, -1]

if __name__ == '__main__':
    matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
  ]
    target= 1000
    print(searchInSortedMatrix(matrix, target))