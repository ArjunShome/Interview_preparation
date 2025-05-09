
def func_summation(number):
    if number == 0:
        return 0
    return number + func_summation(number - 1)

def func_factorial(number):
    if number == 1:
        return 1
    return number * func_factorial(number - 1)


if __name__ =="__main__":
    number = int(input("Enter the number to print the summation: "))
    # print(func_summation(number))
    print(func_factorial(number))