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
    def get_engine_details(self):
        pass

    @abstractmethod
    def size(self):
        pass


class SUV(Vehicle):
    def get_engine_details(self):
        print("Engine details of SUV")

    def size(self):
        print("Size of SUV is above 4 meters in length")

    def drive_off_road(self):
        print("Can Drive Off road")

    def drive_on_road(self):
        print("Can Drive On road")


class Compact(Vehicle):
    def get_engine_details(self):
        print("Engine details of Compact")

    def size(self):
        print("Size of Compact is below 4 meters in length")

    def drive_on_road(self):
        print("Recommended to Drive Only On road")


class SportsBike(Vehicle):
    def get_engine_details(self):
        print("Engine details of Sports Bike")

    def size(self):
        print("Size of Sports Bike is below 2 meters in length")

    def ride(self):
        print("Riding Sports Bike")


class GrandI10(Compact):
    def get_engine_details(self):
        print("Engine details of Grad I10 -> Kappa 1.2L, 4-cylinder")

    def size(self):
        print("Size of Grad I10 -> Compact")

    def drive_on_road(self):
        print("Driving Grad I10")


class Creta(SUV):
    def get_engine_details(self):
        print("Engine details of Creta -> 1.5L, 4-cylinder")

    def size(self):
        print("Size of Creta -> Mid-size SUV")

    def drive_on_road(self):
        print("Driving Creta")

    def drive_off_road(self):
        print("Driving Creta Off road")


class Safari(SUV):
    def get_engine_details(self):
        print("Engine details of Creta -> 2.0L, 4-cylinder")

    def size(self):
        print("Size of Safari -> Full-size SUV")

    def drive_on_road(self):
        print("Driving Safari")

    def drive_off_road(self):
        print("Driving Safari Off road")


class RS200(SportsBike):
    def get_engine_details(self):
        print("Engine details of RS200 -> 199.5cc, Single-cylinder, Liquid-cooled")

    def size(self):
        print("Size of RS200 -> Sport Bike")

    def ride(self):
        print("Riding RS200")


class VehiclePricing(ABC):
    @abstractmethod
    def calculate_vehicle_price(self):
        pass


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


class RS200Pricing(VehiclePricing):

    def __init__(self, city: str):
        self.city = city

    def calculate_vehicle_price(self):
        if self.city.lower() == City.Kolkata:
            print("Price of RS200 -> Rs 1,50,000, including 15k Road tax")
        if self.city.lower() == City.Chennai:
            print("Price of RS200 -> Rs 1,55,000, including 16k Road tax")
        if self.city.lower() == City.Mumbai:
            print("Price of RS200 -> Rs 1,60,000, including 18k Road tax")
        if self.city.lower() == City.Hyderabad:
            print("Price of RS200 -> Rs 1,58,000, including 17k Road tax")

def get_suv_vehicle_engine_details_violates_dep_inv():
    # This violates the Dependency Inversion Principle where we are depending on a concrete class
    # In future if there is another type of SUV we want to check engine details for, we will have to modify this function
    suv = Creta()
    suv.get_engine_details()

def get_suv_vehicle_engine_details(suv: SUV):
    # Satisfies the Dependency Inversion Principle where we depend on an abstraction
    suv.get_engine_details()

if __name__=='__main__':
    vehicle = Creta()
    vehicle_2 = Safari()
    get_suv_vehicle_engine_details(vehicle)
    get_suv_vehicle_engine_details(vehicle_2)


"""
Why this above class follows Dependency Inversion Principle?
1. High-Level Modules Should Not Depend on Low-Level Modules: Both should depend on Abstractions.
   - In the function `get_suv_vehicle_engine_details`, we depend on the abstraction `SUV` rather than a concrete class like `Creta` or `Safari`.
   - This allows us to pass any SUV type (like `Creta`, `Safari`, or any future SUV) without changing the function.
2. Abstractions Should Not Depend on Details: Details should depend on Abstractions.
    - The `SUV` class is an abstraction that defines the contract for all SUV types.
    - Concrete implementations like `Creta` and `Safari` depend on this abstraction, ensuring that high-level modules (like our function) do not depend on low-level details.
"""
