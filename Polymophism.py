# vehicles_polymorphism.py

# Base Class (optional, just for structure)
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

# Subclasses with their own move() definitions
class Car(Vehicle):
    def move(self):
        print("Roadtripping in the car")

class Plane(Vehicle):
    def move(self):
        print("Enjoying the birds flying")

class Bicycle(Vehicle):
    def move(self):
        print("Riding on the bike lane")

class Boat(Vehicle):
    def move(self):
        print("Sailing along the mulky waters")


# Example usage
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Bicycle(), Boat()]

    for v in vehicles:
        v.move()  # Each class prints its unique move() action
