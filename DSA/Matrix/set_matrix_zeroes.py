
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def set_matrix_zeros(self):
        """ Using two auxilliary array to figure out the rtows and columns
        to be marked as 0.

        Returns:
            _type_: _description_
        """
        rows = len(self.matrix)
        cols = len(self.matrix[0])

        row_marker = [False] * rows
        col_marker = [False] * cols

        for i in range(rows):
            for j in range(cols):
                if self.matrix[i][j] == 0:
                    row_marker[i] = True
                    col_marker[j] = True
        for i in range(rows):
            for j in range(cols):
                if row_marker[i] or col_marker[j]:
                    self.matrix[i][j] = 0
        return self.matrix
    

    def set_matrix_zeros_space_optimized(self):
        """ No Auxiliary arrays required, saves space complexity.

        Returns:
            _type_: _description_
        """
        rows = len(self.matrix)
        cols = len(self.matrix[0])

        firstr_col_zero = False

        # If first row and column is 0
        if self.matrix[0][0] == 0:
            firstr_col_zero = True

        for i in range(rows):
            for j in range(cols):
                 if self.matrix[i][j] == 0:
                      self.matrix[0][j] = 0
                      self.matrix[0][0] = 0
                      self.matrix[i][0] = 0
        
        for i in range(1, rows):
            for j in range(1, cols):
                if self.matrix[0][j] == 0 or self.matrix[i][0] == 0:
                    self.matrix[i][j] = 0
        
        if firstr_col_zero:
             self.matrix[0][:] = [0] * cols
             for el in range(rows):
                 self.matrix[el][0] = 0

        return self.matrix
                
                


if __name__ == '__main__':
    matrix_inp = input("Enter the numbers seperated by comma, in differrent list sperated by (colon :) : ")
    matrix = []
    for row in matrix_inp.split(":"):
        matrix.append([int(el) for el in row.split(",")]) 
    mtrx = Matrix(matrix=matrix)
    # for lst in mtrx.set_matrix_zeros():
    #     print(f'{lst}')
    # print()
    for lst in mtrx.set_matrix_zeros_space_optimized():
        print(f'{lst}')