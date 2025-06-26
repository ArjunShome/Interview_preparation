
class RorateMatrix:
    def __init__(self, array):
        self.matrix = array

    def rotate_array_by_90_degree(self):
        # Rotate the matrix by 90 degrees clockwise.
        rows = len(self.matrix)
        cols = len(self.matrix[0])

        #Transpose
        for i in range(rows-1):
            for j in range(i, cols):
                temp = self.matrix[i][j]
                self.matrix[i][j] = self.matrix[j][i]
                self.matrix[j][i] = temp

        # Reverse the rows in matrix
        for row in range(rows):
            self.matrix[row] = self.matrix[row][::-1]

        return self.matrix

if __name__ == '__main__':
    inp_lst = input("Enter the numbers sperated by comma and differrent rows by colon (:) :")
    inp_arr = []
    for el in inp_lst.split(":"):
        inp_arr.append([int(num) for num in el.split(",")])
    mtx = RorateMatrix(inp_arr)
    for row in mtx.rotate_array_by_90_degree():
        print(row)
    