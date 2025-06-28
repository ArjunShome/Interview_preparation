
class ThreeSumProblem:
    def __init__(self, array):
        self.array = sorted(array)
    

    def find_three_sum_from_array_optimal(self):
        i = 0
        j = i+1
        k = len(self.array) - 1
        lst = []

        while j <= k:
            sum = self.array[i] + self.array[j] + self.array[k]
            if sum == 0:
                lst.append([self.array[i],self.array[j],self.array[k]])
                j += 1
                k -= 1
            if sum < 0:
                j += 1
            i+=1
        return lst
        


if __name__ == '__main__':
    input_arr = input("Enter the array of elements seperated by comma: ")
    input_arr = [int(el) for el in input_arr.split(",")]
    tsm = ThreeSumProblem(input_arr)
    st_output = tsm.find_three_sum_from_array()
    st_output_2 = tsm.find_three_sum_from_array_optimal()
    print(st_output)
    print(st_output_2)
