

class SpriralMtrxPrint:
    def __init__(self, mtrx):
        self.matrix = mtrx

    def get_spiral_of_a_matrix(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])

        top,left = 0,0
        right = rows 
        bottom = cols
        spriral_order = []

        while(left <= right):
            # Traverse from left to right 
            for i in range(right):
                spriral_order.append(self.matrix[left][i])
            top += 1
            right -= 1
            # Traverse from right to bottom
            for j in range(top, bottom-1):
                spriral_order.append(self.matrix[j][bottom-1])
            # Traverse from bottom to left
            for k in range(right, left, -1):
                spriral_order.append(self.matrix[bottom-1][k])
            bottom -= 1
            # Traverse from left to top
            for l in range(bottom, top, -1):
                spriral_order.append(self.matrix[l][left])
            left += 1
        return spriral_order


if __name__ == '__main__':
    input = input("Enter the numbers sepreated by comma and lists seperated by colons: ")
    inp_mtrx = []
    for lst in input.split(":"):
        inp_mtrx.append([int(el) for el in lst.split(",")])
    spriral_mtrx = SpriralMtrxPrint(inp_mtrx)
    print(spriral_mtrx.get_spiral_of_a_matrix())
    
