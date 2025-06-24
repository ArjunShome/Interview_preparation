
class NextPermutationArray:
    def __init__(self, array):
        self.array = array

    def generate_next_permutation(self):
        breakout_index = -1
        for i in range(len(self.array)-2, 0, -1):
            if self.array[i] < self.array[i+1]:
                breakout_index = i
                break
        for j in range(len(self.array) - 1, breakout_index, -1):
            if self.array[j] > self.array[breakout_index]:
                self.replace(self.array, j, breakout_index)
                break
        self.array = self.array[: breakout_index + 1] + sorted(self.array[breakout_index + 1 :])
        return self.array

    def replace(self, array, indx_1, indx_2):
        temp = array[indx_1]
        array[indx_1] = array[indx_2]
        array[indx_2] = temp

if __name__ == "__main__":
    inp_arr = input("Enter the numbers seperated by comma: ")
    inp_arr = [int(el) for el in inp_arr.split(",")]
    np = NextPermutationArray(inp_arr)
    print(np.generate_next_permutation())
