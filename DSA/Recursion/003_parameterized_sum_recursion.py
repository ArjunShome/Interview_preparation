

def param_sum(i, sum):
    if i < 1:
        print(sum)
        return
    param_sum(i-1, sum+i)

if __name__=="__main__":
    number = int(input("Enter the number to prints its sum till 1: "))
    sum = 0
    param_sum(number, sum)