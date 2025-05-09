# Print Nth fibonacci number
def print_fibonacci(number):
    if number <= 1:
        return number
    first = print_fibonacci(number - 1)
    second = print_fibonacci(number - 2)
    return first + second

if __name__=="__main__":
    number = int(input("Enter the number to print fibonacci upto: "))
    print(print_fibonacci(number))
    for i in range(number):
        print(print_fibonacci(i), end=" ")