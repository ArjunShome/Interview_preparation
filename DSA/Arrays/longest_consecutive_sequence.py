

class ArrayConsequtiveSeq:
    def __init__(self, array):
        self.array = array

    def get_consecutive_sequence(self):
        seek = set(self.array)
        count = 0
        largest_count = 0
        for num in seek:
            if num - 1 in seek:
                continue
            while(True):
                if num + 1 in seek:
                    count += 1
                    num += 1
                else:
                    largest_count = max(largest_count, count + 1)
                    count = 0
                    break
        return largest_count
                

            



if __name__ == '__main__':
    inp_arr = input("Enter the numbers seperated by a space : ")
    inp_arr = [int(el) for el in inp_arr.split(",")]
    ac = ArrayConsequtiveSeq(inp_arr)
    print(ac.get_consecutive_sequence())