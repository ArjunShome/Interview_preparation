# Create a class and enforce that all objects inheriting that class ahas a "sum" method
import sys


class MetaSum(type):
    def __new__(cls, name, bases, attrs):
        print(f"Class Name = {name}")
        print(f"Class Attributes = {attrs}")
        if "sum" not in attrs:
            raise TypeError("ERROR - Must implement the sum method")
        return super().__new__(cls, name, bases, attrs)

try:
    class CalcSum(metaclass=MetaSum):
        m = 10
        n = 20

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def check_bal(self):
            print("Hi")

        def sum(self):
            print(self.x + self.y)

    class Build(metaclass=MetaSum):
        def show(self):
            print("Hi")

        def sum(self):
            print("Summed")

except TypeError as te:
    print(str(te))
    sys.exit(0)


if __name__=="__main__":
    cs = CalcSum(x=5, y=10)
    cs.check_bal()

    b = Build()
    b.show()