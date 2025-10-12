"""
Create a custom iterator class called ReverseIterator that:
	•	Accepts a list during initialization.
	•	Iterates from the last element to the first (reverse order).
	•	Implements the correct iterator protocol using __iter__() and __next__().
	•	Raises StopIteration exactly at the correct time (no extra next() after completion).
	•	Works manually with next() and inside a for loop.

    
Expected Usage - 
rev = ReverseIterator([10, 20, 30, 40])

print(next(rev))  # 40
print(next(rev))  # 30

for item in rev:
    print(item)   # continues with 20, 10

    
 Bonus (Optional for extra evaluation):
	•	Add support for resetting iteration using a .reset() method.
	•	Make it also work with Python’s built-in reversed() if someone wraps it.
"""


class ReverseIterator:
    def __init__(self, usr_lst):
        self.user_list = usr_lst[::-1]
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.user_list):
            raise StopIteration
        item = self.user_list[self.index]
        self.index += 1
        return item


if __name__=='__main__':
    user_list = ['Arjun', 'Ayan', 'Ajoy', 'Rama', 'Sanchita', 'Manjusa']
    reversed = ReverseIterator(usr_lst=user_list)
    print(next(reversed))
    print(next(reversed))
    for el in reversed:
        print(el)