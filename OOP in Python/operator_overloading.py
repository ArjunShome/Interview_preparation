
class Calculate:
    def __init__(self, m, n):
        self.val1 = m
        self.val2 = n

    # Addition
    def __add__(self, other):
        self.obj1_sum = self.val1 + self.val2
        self.obj2_sum = other.val1 + other.val2
        return self.obj1_sum + self.obj2_sum

    # Substraction
    def __sub__(self, other):
        self.obj1_sub = self.val1 - self.val2
        self.obj2_sub = other.val1 - other.val2
        return self.obj1_sub - self.obj2_sub

    # Multiplication
    def __mul__(self, other):
        self.obj1_mul = self.val1 * self.val2
        self.obj2_mul = other.val1 * other.val2
        return self.obj1_mul * self.obj2_mul

    # Greater than, by checking the sum of the two values
    def __gt__(self, other):
        self.obj1_gt = self.val1 + self.val2
        self.obj2_gt = other.val1 + other.val2
        if self.obj1_gt > self.obj2_gt:
            return True
        return False

    # Equal to
    def __eq__(self, other):
        self.obj1 = self.val1 + self.val2
        self.obj2 = other.val1 + other.val2
        if self.obj1 == self.obj2:
            return True
        return False

    # Less than
    def __lt__(self, other):
        self.obj1_lt = self.val1 + self.val2
        self.obj2_lt = other.val1 + other.val2
        if self.obj1_lt < self.obj2_lt:
            return True
        return False

    def __le__(self, other):
        self.obj1_le = self.val1 + self.val2
        self.obj2_le = other.val1 + other.val2
        if self.obj1_le <= self.obj2_le:
            return True
        return False

    #string representation
    def __str__(self):
        return f"This is the Calculate class having the instance values {self.val1} and {self.val2}"

calc = Calculate(10, 20)
calc2 = Calculate(10,70)

print(calc + calc2)
print(calc - calc2)
print(calc * calc2)
print(calc > calc2)
print(calc2 > calc)
print(calc == calc2)
print(calc < calc2)
print(calc <= calc2)
print(str(calc))
print(str(calc2))