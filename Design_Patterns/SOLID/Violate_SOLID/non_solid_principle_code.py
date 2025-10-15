
from enum import Enum

class VehicleName(Enum):
    Grand_I10 = "grand_i10"
    Creta = "creta"

class City(Enum):
    Mumbai = "mumbai"
    Kolkata = "kolkata"
    Chennai = "chennai"
    Hyderabad = "hyderabad"


class Vehicle:

    def __init__(self, name):
        self.name = name

    def drive(self):
        if self.name.lower() == VehicleName.Grand_I10:
            print("Driving Grad I10")
        elif self.name.lower() == VehicleName.Creta:
            print("Driving Creta")
        else:
            print("Driving unknown vehicle")

    def get_engine_details(self):
        if self.name.lower() == VehicleName.Grand_I10:
            print("Engine details of Grad I10 -> Kappa 1.2L, 4-cylinder")
        if self.name.lower() == VehicleName.Creta:
            print("Engine details of Creta -> 1.5L, 4-cylinder")

    def size(self):
        if self.name.lower() == VehicleName.Grand_I10:
            print("Size of Grad I10 -> Compact")
        if self.name.lower() == VehicleName.Creta:
            print("Size of Creta -> Mid-size SUV")

    def get_vehicle_price(self, city):
        if city.lower() == City.Kolkata:
            if self.name.lower() == VehicleName.Grand_I10:
                print("Price of Grad I10 -> Rs 615,000, including 40k Road tax")
            else:
                print("Price of Creta -> Rs 18,00,000, including 95k Road tax")
        if city.lower() == City.Chennai:
            if self.name.lower() == VehicleName.Grand_I10:
                print("Price of Grad I10 -> Rs 630,000, including 55k Road tax")
            else:
                print("Price of Creta -> Rs 18,10,000, including 10.55k Road tax")
        if city.lower() == City.Mumbai:
            if self.name.lower() == VehicleName.Grand_I10:
                print("Price of Grad I10 -> Rs 637,000, including 62k Road tax")
            else:
                print("Price of Creta -> Rs 19,00,000, including 11.55k Road tax")
        if city.lower() == City.Mumbai:
            if self.name.lower() == VehicleName.Grand_I10:
                print("Price of Grad I10 -> Rs 635,000, including 60k Road tax")
            else:
                print("Price of Creta -> Rs 18,30,000, including 10.80k Road tax")


"""
Why this above class Violates the SOLID principles?
1. Single Responsibility Principle (SRP) Violation:
   - The Vehicle class has multiple responsibilities: driving the vehicle, getting engine details, determining size, and calculating price based on city. Each of these functionalities should ideally be in separate classes.
2. Open/Closed Principle (OCP) Violation:
   - The Vehicle class is not closed for modification. If a new vehicle type is added, the class needs to be modified to include new conditions for that vehicle, which violates the OCP.
3. Liskov Substitution Principle (LSP) Violation:
   - If we were to create subclasses for different vehicle types, they might not be able to substitute the base Vehicle class without altering the expected behavior, especially if they have different implementations for methods like get_vehicle_price.
4. Interface Segregation Principle (ISP) Violation:
   - The Vehicle class forces clients to depend on methods they do not use. For example, a client interested only in engine details would still have to deal with methods related to driving and pricing.
5. Dependency Inversion Principle (DIP) Violation:
   - The Vehicle class depends on concrete implementations (specific vehicle names and cities) rather than abstractions. This makes it difficult to change or extend the code without modifying the Vehicle class itself.
   
Our task here will be to refactor this code to support the SOLID principles. We will be doing that in different files outside this current folder.
"""



