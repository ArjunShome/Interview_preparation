
def rearrange(array):
    pos = []
    neg = []
    temp_arr = []
    for i in array:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)

    if len(pos) > len(neg):
        for i in range(len(neg)):
            temp_arr.insert(i*2, pos[i])
            temp_arr.insert(i*2 +1, neg[i])
        for i in range(len(neg), len(pos)):
            temp_arr.append(pos[i])
    else:
        for i in range(len(pos)):
            temp_arr.insert(i*2, pos[i])
            temp_arr.insert(i*2 + 1, neg[i])
        for i in range(len(pos), len(neg)):
            temp_arr.append(neg[i])
    return temp_arr


if __name__ == "__main__":
    inp_arr = input("Enter the numbers : ")
    lst_arr = [int(el) for el in inp_arr.split(",")]
    print(rearrange(lst_arr))
