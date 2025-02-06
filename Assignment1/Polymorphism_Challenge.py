# Base class for Vehicle
class Vehicle:
    def move(self):
        # This method will be overridden by subclasses
        pass

# Subclass for Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass for Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass for Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Function to demonstrate polymorphism
def demonstrate_move(vehicle):
    vehicle.move()

# Example usage:
car = Car()
plane = Plane()
boat = Boat()

# Demonstrating polymorphism
demonstrate_move(car)  # Output: Driving 🚗
demonstrate_move(plane)  # Output: Flying ✈️
demonstrate_move(boat)  # Output: Sailing 🚤
