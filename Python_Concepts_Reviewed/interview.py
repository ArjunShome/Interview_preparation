
# Input
# [1 ,2 ,6 ,3 ,7 ,4 ,2 ,3]

# Output
# [2 ,3]


def get_duplicates(array: list[int]) -> list[int]:
    seen = {}
    output_lst = []
    for el in array:
        if el in seen:
            output_lst.append(el)
        else:
            seen[el]= 1
    return output_lst


if __name__=='__main__':
    input_array = [1 ,2 ,6 ,3 ,7 ,4 ,2 ,3]
    print(get_duplicates(input_array))