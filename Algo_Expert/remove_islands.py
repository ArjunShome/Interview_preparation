def removeIslands(matrix):
    # Write your code here.
    vertices_connected_to_border = [[False for j in matrix[0]] for i in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            row_in_border = row == 0 or row == len(matrix) - 1
            col_in_border = col == 0 or col == len(matrix[row]) - 1
            is_border = row_in_border or col_in_border

            if not is_border:
                continue

            if matrix[row][col] != 1:
                continue

            find_neighbours_connected_to_border(row, col, matrix, vertices_connected_to_border)

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[0]) - 1):
            if vertices_connected_to_border[row][col]:
                continue
            
            matrix[row][col] = 0
    
    return matrix


def find_neighbours_connected_to_border(start_row, start_col, matrix, vertices_connected_to_border):
    stack = [(start_row, start_col)]

    while len(stack) > 0:
        current = stack.pop()
        cur_row, cur_col = current

        already_visited = vertices_connected_to_border[cur_row][cur_col]
        
        if already_visited:
            continue

        vertices_connected_to_border[cur_row][cur_col] = True

        neighbours = get_neighbours(cur_row, cur_col, matrix)

        for neighbour in neighbours:
            row, col = neighbour
            if matrix[row][col] == 1:
                stack.append((row, col))


def get_neighbours(row, col, matrix):
    neighbours = []
    num_rows = len(matrix)
    num_cols = len(matrix[row])

    if row - 1 >= 0:
        neighbours.append((row - 1, col)) # UP

    if row + 1 < num_rows:
        neighbours.append((row + 1, col)) # DOWN

    if col - 1 >= 0:
        neighbours.append((row, col - 1)) # LEFT

    if col + 1 < num_cols:
        neighbours.append((row, col + 1)) # RIGHT

    return neighbours


        

if __name__ == '__main__':
    matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
    ]
    print(removeIslands(matrix))
