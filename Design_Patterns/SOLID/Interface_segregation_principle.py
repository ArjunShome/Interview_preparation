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


class VehiclePricing(ABC):
    @abstractmethod
    def calculate_vehicle_price(self):
        pass


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


class RS200(SportsBike):
    def get_engine_details(self):
        print("Engine details of RS200 -> 199.5cc, Single-cylinder, Liquid-cooled")

    def size(self):
        print("Size of RS200 -> Sport Bike")

    def ride(self):
        print("Riding RS200")


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


"""
Why the above follows Interface Segregation Principle?
1. Clients should not be forced to depend on interfaces they do not use: The Vehicle class is split into more specific classes 
    (SUV, Compact, SportsBike), each with methods relevant to their type. This way, a client using a Compact vehicle does not need to implement
    methods related to off-road driving, which are irrelevant to it.
"""