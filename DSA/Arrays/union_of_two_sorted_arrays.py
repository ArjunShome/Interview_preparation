

class Array:
    def __init__(self, array1, array2):
        self .array1 = array1
        self.array2 = array2

    def union_of_two_sorted_arrays(self):
        j = 0
        i = 0
        ar1sz = len(self.array1)
        ar2sz = len(self.array2)
        temp_arr = []
        seen = set()

        while(i < ar1sz and j < ar2sz):
            if self.array1[i] < self.array2[j]:
                val = self.array1[i]
                i += 1
            else:
                val = self.array2[j]
                j += 1
            
            if val not in seen:
                temp_arr.append(val)
                seen.add(val)
        
        while(i< ar1sz):
            if self.array1[i] not in seen:
                temp_arr.append(self.array1[i])
                seen.add(val)
            i += 1

        while(j < ar2sz):
            if self.array2[j] not in seen:
                temp_arr.append(self.array2[j])
                seen.add(val)
            j += 1

        return temp_arr


if __name__ == "__main__":
    input_array1 = input("Enter the first sorted array of numbers separated by comma: ")
    input_array1 = [int(number) for number in input_array1.split(",")]
    input_array2 = input("Enter the second sorted array of numbers separated by comma: ")
    input_array2 = [int(number) for number in input_array2.split(",")]

    array_instance = Array(input_array1, input_array2)
    union_array = array_instance.union_of_two_sorted_arrays()
    print(f"Union of two sorted arrays: {union_array}")
