"""
Implement a class hierarchy:
	1.	Shape (abstract base class)
	•	Abstract methods: area(), perimeter()
	•	name attribute (read-only property)
	•	__repr__ shows class name and constructor args

	2.	Rectangle(Shape)
	•	width, height (validate: > 0 via property setters)
	•	Implements area, perimeter
	•	Overrides __eq__ to compare by area (tolerance 1e-9)

	3.	Circle(Shape)
	•	radius (validate: > 0)
	•	Implements area, perimeter

	4.	Triangle(Shape)
	•	a, b, c sides (validate triangle inequality; all > 0)
	•	Implements area (Heron’s formula) and perimeter

	5.	JSONMixin
	•	to_dict() returns a serializable dict of public fields
	•	to_json(indent=2) dumps that dict as JSON

Make RectangleJSON(Rectangle, JSONMixin) and CircleJSON(Circle, JSONMixin) to test multiple inheritance.

Functional Requirements
	•	Use abc.ABC and @abstractmethod
	•	Use super() correctly in constructors and __repr__
	•	Input validation via properties; raise ValueError on bad inputs
	•	Polymorphism: a function total_area(shapes: list[Shape]) -> float that sums areas
	•	Demonstrate MRO works for to_json() on RectangleJSON/CircleJSON

Expected Usage (you don’t need to print these exact numbers, but logic must work)

r = Rectangle(3, 4)
c = Circle(1)
t = Triangle(3, 4, 5)

assert round(r.area(), 5) == 12
assert round(c.perimeter(), 5) == 2 * 3.14159  # approx
assert round(t.area(), 5) == 6                 # 3-4-5 triangle

# equality by area
assert Rectangle(2, 6) == Rectangle(3, 4)

# polymorphism
assert round(total_area([r, c, t]), 5) > 0

# mixin + MRO
rj = RectangleJSON(2, 5)
print(rj.to_json())  # valid JSON string

Bonus (optional, for deeper evaluation)
	•	Add Square(Rectangle) that reuses Rectangle validation and keeps sides equal.
	•	Implement caching for area() using functools.cached_property and invalidate on dimension change.

"""

from abc import ABC, abstractmethod
import math
import json

class Shape(ABC):

    def __init__(self):
        super().__init__()
        self._name = self.__class__.__name__

    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    
    @abstractmethod
    def validate_params(self):
        pass

    def __repr__(self):
        fields = ", ".join(f"{k} = {v!r}" for k, v in vars(self).items() if not k.startswith("_"))
        return f"{self.__class__.__name__}({fields})"
    

class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length
        self.validate_params()

    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2 * (self.width + self.length)
    
    def validate_params(self):
        if self.width < 1 or self.length < 1:
            raise ValueError("Width / length cannot be less than 1")
    
    def __eq__(self, other):
        if self.area() == other.area():
            return True
        return False
    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.validate_params()

    def area(self):
        return math.pi * (self.radius * self.radius)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def validate_params(self):
        if self.radius < 1:
            raise ValueError("Radius cannot be less than 1")
    

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.validate_params()

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def validate_params(self):
        if self.a < 1 or self.b < 1 or self.c < 1:
            raise ValueError("Values cannot be less than 1")
    

class JSONMixin:
    def to_dict(self):
        return {k: v for k, v in vars(self).items() if not k.startswith('_')}
    
    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)
    
class RectangleJson(JSONMixin, Rectangle):
    def __init__(self, width, length):
        super().__init__(width, length)


class CircleJson(JSONMixin, Circle):
    def __init__(self, radius):
        super().__init__(radius)


def total_area(shapes: list[Shape]) -> float:
    calc_sum = 0
    for shape in shapes:
        calc_sum += shape.area()
    return calc_sum


if __name__=='__main__':
    r = Rectangle(3, 4)
    c = Circle(1)
    t = Triangle(3, 4, 5)

    print(r.area())
    print(c.area())
    print(c.perimeter())
    print(t.area())
    print(total_area([r,c,t]))

    assert round(r.area(), 5) == 12
    assert round(c.perimeter(), 2) == round(2 * 3.14159, 2)  # approx
    assert round(t.area(), 5) == 6                 # 3-4-5 triangle

    assert Rectangle(2,3) == Rectangle(3, 2)

    assert round(total_area([r, c, t]), 5) > 0

    rj = RectangleJson(2, 5)
    print(rj.to_json())  # valid JSON string

    cj = CircleJson(2)
    print(cj.to_json())

    print(str(r))
    print(str(c))
    print(str(t))
    print(RectangleJson.mro())

