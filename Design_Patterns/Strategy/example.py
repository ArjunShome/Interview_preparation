from abc import ABC, abstractmethod
from random import random

# Price Promotion Engine

class PromotionStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass

class NoDiscount(PromotionStrategy):
    def apply_discount(self, price: float) -> float:
        print("No Discount Applied")
        return price

class PercentDiscount(PromotionStrategy):
    def __init__(self, discount_percent: float) -> None:
        self.discount_percent = discount_percent

    def apply_discount(self, price: float) -> float:
        discount_amount = price * (self.discount_percent / 100)
        print(f"Applying {self.discount_percent}% Discount: -₹{discount_amount:.2f}")
        return price - discount_amount

class AdditionalProductWithPurchase(PromotionStrategy):
    def __init__(self, product1: int, product2: int, unit_price: float, unit_qty: int) -> None:
        self.product_1 = product1
        self.product_2 = product2
        self.unit_price = unit_price
        self.unit_qty = unit_qty
        self.promotional_unit = 0

    def apply_discount(self, price: float) -> float:
        if self.unit_qty <= 6 :
            self.promotional_unit = 1
        elif self.unit_qty > 6:
            self.promotional_unit = 2
        print(f"Applying Promotional offer of extra {self.promotional_unit} unit(s) of product -> {self.product_2} free, on purtchase of {self.unit_qty} unit(s) of product -> {self.product_1}")
        return self.unit_qty * self.unit_price

# Client Code
class PromotionEngine:
    def __init__(self, strategy: 'PromotionStrategy') -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: 'PromotionStrategy') -> None:
        self._strategy = strategy

    def total_price(self, price: float) -> float:
        return self._strategy.apply_discount(price)

def print_price(engine: PromotionEngine):
    print(f"Total Price -> {engine.total_price(bill)}")

if __name__== '__main__':
    # No Discount
    bill = 12000
    quantity = 12
    unit_price = 1000
    id = 111
    promotional_products = [2, 6, 7, 143, 154]

    engine = PromotionEngine(NoDiscount())
    print_price(engine)

    engine.set_strategy(PercentDiscount(10))
    print_price(engine)

    promotion_choice = int(input(f"Enter you choice of products among these {promotional_products}"))
    engine.set_strategy(AdditionalProductWithPurchase(product1=id, product2=promotion_choice, unit_qty=quantity, unit_price=unit_price))
    print_price(engine)