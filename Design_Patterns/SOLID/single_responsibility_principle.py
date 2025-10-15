"""
Supporting Only Single Responsibility Principle here
"""
from abc import ABC, abstractmethod
from enum import Enum

class VehicleName(Enum):
    Grand_I10 = "grand_i10"
    Creta = "creta"

class City(Enum):
    Mumbai = "mumbai"
    Kolkata = "kolkata"
    Chennai = "chennai"
    Hyderabad = "hyderabad"


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def get_engine_details(self):
        pass

    @abstractmethod
    def size(self):
        pass


class VehiclePricing(ABC):

    @abstractmethod
    def calculate_vehicle_price(self):
        pass


class GrandI10(Vehicle):

    def drive(self):
        print("Driving Grad I10")

    def get_engine_details(self):
        print("Engine details of Grad I10 -> Kappa 1.2L, 4-cylinder")

    def size(self):
        print("Size of Grad I10 -> Compact")


class Creta(Vehicle):

    def drive(self):
        print("Driving Creta")

    def get_engine_details(self):
        print("Engine details of Creta -> 1.5L, 4-cylinder")

    def size(self):
        print("Size of Creta -> Mid-size SUV")

class GrandI10Pricing(VehiclePricing):

    def __init__(self, city: str):
        self.city = city

    def calculate_vehicle_price(self):
        if self.city.lower() == City.Kolkata:
            print("Price of Grad I10 -> Rs 615,000, including 40k Road tax")
        if self.city.lower() == City.Chennai:
            print("Price of Grad I10 -> Rs 630,000, including 55k Road tax")
        if self.city.lower() == City.Mumbai:
            print("Price of Grad I10 -> Rs 637,000, including 62k Road tax")
        if self.city.lower() == City.Hyderabad:
            print("Price of Grad I10 -> Rs 635,000, including 60k Road tax")

class CretaPricing(VehiclePricing):

    def __init__(self, city: str):
        self.city = city

    def calculate_vehicle_price(self):
        if self.city.lower() == City.Kolkata:
            print("Price of Creta -> Rs 18,00,000, including 95k Road tax")
        if self.city.lower() == City.Chennai:
            print("Price of Creta -> Rs 18,10,000, including 10.55k Road tax")
        if self.city.lower() == City.Mumbai:
            print("Price of Creta -> Rs 19,00,000, including 11.55k Road tax")
        if self.city.lower() == City.Hyderabad:
            print("Price of Creta -> Rs 18,30,000, including 10.80k Road tax")


"""
Why the above class follows single Responsibility Principle?
1. Single Responsibility Principle (SRP) Adherence: Each class has a single responsibility:
   - Vehicle classes (GrandI10, Creta) handle vehicle-specific behaviors like driving, engine details, and size.
   - Pricing classes (GrandI10Pricing, CretaPricing) handle the pricing logic based on the city.
This separation of concerns makes the code more maintainable and easier to understand.
"""