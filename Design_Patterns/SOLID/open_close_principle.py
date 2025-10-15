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


class RS200(Vehicle):

    def drive(self):
        print("Driving RS200")

    def get_engine_details(self):
        print("Engine details of RS200 -> 199.5cc, Single-cylinder, Liquid-cooled")

    def size(self):
        print("Size of RS200 -> Sport Bike")


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
Why the above class follows open close Principle?
1. Open for Extension: The design allows for the addition of new vehicle types (e.g., RS200) and their pricing strategies 
    without modifying existing classes. 
    New vehicle classes can be created by inheriting from the Vehicle abstract base class, and new pricing classes can be 
    created by inheriting from the VehiclePricing abstract base class.
2. Closed for Modification: Existing classes (GrandI10, Creta, GrandI10Pricing, CretaPricing) do not need to be changed 
    when new vehicle types or pricing strategies are added. This reduces the risk of introducing bugs into existing code.
"""