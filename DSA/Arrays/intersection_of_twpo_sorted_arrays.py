class Array:
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2

    def intersection_of_array(self):
        i,j = [0,0]
        arsz1 = len(self.array1)
        arsz2 = len(self.array2)
        intersection = []
        seen = set()

        while i< arsz1 and j < arsz2:
            if self.array1[i] == self.array2[j]:
                val = self.array1[i]
                if val not in seen:
                    intersection.append(val)
                    seen.add(val)
                i+=1
                j+=1
            else:
                i+=1
        return intersection
    

if __name__ == "__main__":
    array1 = [2,3,4,5,6,7,8,9,0]
    array2 = [2, 3, 5, 6, 7]
    arr = Array(array1, array2)
    print("Intersection of two sorted arrays is:", arr.intersection_of_array())
