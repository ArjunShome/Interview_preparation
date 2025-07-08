
def transposeMatrix(matrix):
    # Write your code here.
    rows = len(matrix) - 1
    columns = len(matrix[0])
    i = 0
    j = 0
    out_mtrx = []
    cur_lst = []
    while i <= rows:
        cur_lst.append(matrix[i][j])
        i += 1
        if i > rows:
            i = 0
            j += 1
            out_mtrx.append(cur_lst)
            cur_lst = []
        if j > columns - 1:
            break
    return out_mtrx





    return []

if __name__ == '__main__':
    matrix= [
    [0, 0, 0],
    [1, 1, 1]
  ]
    print(transposeMatrix(matrix))