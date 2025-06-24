
class LeaderInArray:
    def __init__(self, arr):
        self.array = arr

    def get_leaders_in_array_brute(self):
        leaders = []
        for i in range(len(self.array)):
            leader = True
            for j in range(i+1, len(self.array)):
                if self.array[j] > self.array[i]:
                    leader = False 
                    break
            if leader:
                leaders.append(self.array[i])
        return leaders
    
    def get_leaders_in_array_optimized(self):
        leaders = []
        max = 0
        for i in range(len(self.array)-1, 0, -1):
            if self.array[i] > max:
                leaders.append(self.array[i])
                max = self.array[i]     
        return leaders


if __name__=="__main__":
    inp_arr = input("Enter the number of elements in the array speerated by comma: ")
    inp_arr = [int(el) for el in inp_arr.split(",")]
    leader = LeaderInArray(inp_arr)
    print(leader.get_leaders_in_array_brute())
    print(leader.get_leaders_in_array_optimized())
