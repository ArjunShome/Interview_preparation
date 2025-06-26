

class MajorityEln3:
    def __init__(self, array):
        self.array = array
        self.array = sorted(self.array)

    def find_majority_nby3(self):
        count = 0
        numbers = []
        dict_num = {}
        el = 0

        for num in self.array:
            if count == 0:               
                el = num
                count += 1
            elif num != el:
                dict_num[el] = count                
                el = num
                count = 1
            elif num == el:
                count += 1

        for key in dict_num:
            if dict_num[key] > int(len(self.array) / 3):
                numbers.append(key)
        
        return numbers
    
if __name__ == "__main__":
    num_input = input("Enter the numbers separated by comma: ")
    numbers = [int(el) for el in num_input.split(",")]
    majority = MajorityEln3(numbers)
    result = majority.find_majority_nby3()
    print(result)
            