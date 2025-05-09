# Base Illusttration of Function calling itself and Recursion.
# If no base condition is given the print will happen for multiple times and then
# Stack Overflow exception will occur, as the calls of every function is loaded in a stack during call.

def print_number(number: int, cnt: int) -> None:
    """
    Print the number.
    """
    print(number)
    cnt +=1
    if cnt == 10:
        return
    else:
        print_number(number, cnt)

if __name__ == "__main__":
    number = 10
    cnt = 0
    print_number(number, cnt)
