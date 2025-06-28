

class MergeSubinterval:
    def __init__(self, array):
        self.array = array

    def get_overlapping_subintervals(self):
        i = 0
        lst_sub_intervals = []

        while(i + 1 < len(self.array)):
            j = i + 1
            i_first, i_last = self.array[i]
            j_first, j_last = self.array[j]
            if i_last < j_first or i_first > j_last:
                i+=1
                continue
            if i_first <= j_last and i_first > j_first:
                if (j_first, i_last) not in lst_sub_intervals:
                    lst_sub_intervals.append((j_first, i_last))
            elif j_first <= i_last and j_last > i_last:
                if (i_first, j_last) not in lst_sub_intervals:
                    lst_sub_intervals.append((i_first, j_last))
            elif i_first <= j_first and i_last >= j_last:
                if (i_first, i_last) not in lst_sub_intervals:
                    lst_sub_intervals.append((i_first, i_last))
            i += 1
        return lst_sub_intervals


if __name__ == '__main__':
    inp_arr = input("Enter the tuples spilt with comma and differrent tuples with colon(:) : ")
    inp_arr_final = []
    for el in inp_arr.split(":"):
        num = int(el.split(",")[0]), int(el.split(",")[1])
        inp_arr_final.append(num)
    ms = MergeSubinterval(inp_arr_final)
    print(ms.get_overlapping_subintervals())
