"""
🧠 Exercise: Closure-Based Counter vs Regular Function

✅ Requirements:
	1.	Write a regular function make_counter_wrong() that attempts to create a counter without using closures.
	•	It should look like it works but fails to correctly persist state between calls.
	•	Example:
        c = make_counter_wrong()
        print(c())  # 1
        print(c())  # 2   <-- should fail or restart due to wrong approach

	2.	Then write a proper closure make_counter() that:
	•	Implements a persistent counter using a closure with nonlocal.
	•	Example:
        counter = make_counter()
        print(counter())  # 1
        print(counter())  # 2
        print(counter())  # 3

    3.	✅ Bonus:
	•	Add another closure make_limited_counter(limit) that:
	•	Stops at a max limit.
	•	Once the limit is reached, it prints "Limit reached" and does not increment further.

🎯 Expected Behavior Demo
    counter = make_counter()
    print(counter())  # 1
    print(counter())  # 2

    bad_counter = make_counter_wrong()
    print(bad_counter())  # 1
    print(bad_counter())  # (Should NOT keep state properly)

    limited = make_limited_counter(3)
    print(limited())  # 1
    print(limited())  # 2
    print(limited())  # 3
    print(limited())  # "Limit reached"
"""


def make_counter_wrong():
    def counter():
        count = 0
        count += 1
        return count
    return counter


def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

def make_limited_counter(limit: int):
    if limit <= 0:
        raise ValueError("limit must be greater than zero")
    count = 0
    def counter():
        nonlocal count
        if count < limit:
            count += 1
            return count
        return None
    return counter


if __name__=='__main__':
    c = make_counter_wrong()
    print(c())  # 1
    print(c())  # 2   <-- should fail or restart due to wrong approach

    print("\nClosure output below\n")
    mc = make_counter()
    print(mc())
    print(mc())
    print(mc())
    print(mc())

    print("\nClosure with limit below\n")
    lc = make_limited_counter(5)
    print(lc())
    print(lc())
    print(lc())
    print(lc())
    print(lc())
    print(lc())
