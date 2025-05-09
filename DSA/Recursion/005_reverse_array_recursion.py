

def reverse_list_numbers(count, list_numbers: list):
    if count == len(list_numbers) - 1:
        return list_numbers
    
    list_numbers.insert(count, list_numbers.pop(-1))
    return reverse_list_numbers(count+1, list_numbers)


if __name__=="__main__":
    numbers = input("Enter the numbers seperated by comma to reverse: ")
    list_numbers = [int(number) for number in numbers.split(",")]
    count = 0
    reversed_list = reverse_list_numbers(count, list_numbers)
    print(reversed_list)
