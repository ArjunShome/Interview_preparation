

def find_majority_mva(num_array):
    "Moore's Voting Alghorithm"
    count = 0
    el = 0
    for num in num_array:
        if count == 0:
            el = num
            count += 1
        elif num != el:
            count -= 1
        elif num == el:
            count += 1

    for num in num_array:
        if num == el:
            count += 1
    if count > len(num_array)/2:
        return el
    else:
        return -1



if __name__ == "__main__":
    num_input = input("Enter the numbers seperated by comma: ")
    numbers = [int(el) for el in num_input.split(",")]
    majority = find_majority_mva(numbers)
    print(majority)