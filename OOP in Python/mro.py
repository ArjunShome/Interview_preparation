

class Shome:
    def show(self):
        print("I amd the House class")

class Dhirendra(Shome):
    def show(self):
        print("I am Dhirendra Chandra Shome")

class Ajoy(Dhirendra, Shome):
    def show(self):
        print("I am the Elder son of Dhirendra Chandra Shome")

class Debabrata(Dhirendra, Shome):
    def show(self):
        print("I am the Younger son of Dhirendra Chandra Shome")

class Arjun(Ajoy, Dhirendra, Shome):
    def show(self):
        print(super(Dhirendra, self).show())
        print("I am the younger Son of Ajoy Shome")

a = Arjun()
a.show()
