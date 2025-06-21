class DNFSort:
    "Dutch National Flag Algorithm for sorting"
    def __init__(self, array):
        self.array = array

    def sort(self):
        low = 0
        mid = 0
        high = len(self.array) - 1

        while mid < high:
            if self.array[mid] == 0:
                self.swap(self.array, low, mid)
                low +=1
                mid +=1

            if self.array[mid] == 1:
                mid +=1

            if self.array[mid] == 2:
                self.swap(self.array, mid, high)
                high -=1

        return self.array


    def swap(self, array, low, high):
        temp = array[low]
        array[low] = array[high]
        array[high] = temp


if __name__=="__main__":
    inputs = input("Enter the numbers of 0, 1, 2 seperated by comma: ")
    list_inputs = [int(el) for el in inputs.split(",")]
    dnf = DNFSort(list_inputs)
    print(dnf.sort())