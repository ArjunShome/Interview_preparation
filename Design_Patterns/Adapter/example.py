from abc import ABC, abstractmethod

# Classes having differrent signature of functions
class Amazon:
    def __init__(self):
        self.cart: list[str] = []

    def add_to_cart(self, item: str) -> None:
        self.cart.append(item)
        print(f"Added {item} to Amazon cart.")

    def do_checkout(self):
        print("Checking out from Amazon with items:", self.cart)
        self.cart.clear()


class Flipkart:
    def __init__(self):
        self.cart: list[str] = []

    def add_item_to_cart(self, item: str) -> None:
        self.cart.append(item)
        print(f"Added {item} to Flipkart cart.")

    def checkout(self):
        print("Checking out from Flipkart with items:", self.cart)
        self.cart.clear()


# Adapter Interfaces
class AddItemToCart(ABC):
    @abstractmethod
    def add_to_cart(self, item: str) -> None:
        pass

class CheckoutCart(ABC):
    @abstractmethod
    def checkout(self):
        pass

# Adapter Classes
class AmazonAdapter(AddItemToCart, CheckoutCart):
    def __init__(self):
        self.amazon = Amazon()

    def add_to_cart(self, item: str) -> None:
        self.amazon.add_to_cart(item)

    def checkout(self):
        self.amazon.do_checkout()

class FlipkartAdapter(AddItemToCart, CheckoutCart):
    def __init__(self):
        self.flipkart = Flipkart()

    def add_to_cart(self, item: str) -> None:
        self.flipkart.add_item_to_cart(item)

    def checkout(self):
        self.flipkart.checkout()



# Client Code
def add_to_cart(provider, item):
    provider.add_to_cart(item)

def checkout(provider):
    provider.checkout()


if __name__=='__main__':
    amazon = AmazonAdapter()
    flipkart = FlipkartAdapter()

    add_to_cart(amazon, "Laptop")
    add_to_cart(amazon, "Smartphone")
    add_to_cart(flipkart, "Headphones")
    add_to_cart(flipkart, "Charger")

    checkout(flipkart)
    checkout(amazon)