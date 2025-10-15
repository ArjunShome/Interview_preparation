

# Class Without Slots
class WithoutSlots:
    def __init__(self, a, b):
        self.a = a
        self.b = b

# Class With Slots
class WithSlots:
    __slots__ = ['a', 'b']

    def __init__(self, a, b, c):
        self.a = a
        self.b = b

    def __sum(self):
        return self.a + self.b

# client
if __name__ == "__main__":
    ws = WithoutSlots(12, 15)
    wts = WithSlots(12, 15, 20)
    # print(wts.__sum())

    print(ws.__dir__())
    print(wts.__dir__())

    print(ws.__dict__)
    print(wts.__dict__)
