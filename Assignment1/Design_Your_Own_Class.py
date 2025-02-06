# Smartphone class with attributes and methods
class Smartphone:
    def __init__(self, brand, model, battery_percentage):
        # Constructor to initialize the object
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
    
    # Method to simulate making a call
    def make_call(self, phone_number):
        print(f"Making a call to {phone_number} from {self.brand} {self.model}...")

    # Method to simulate charging the smartphone
    def charge(self, charge_amount):
        self.battery_percentage += charge_amount
        if self.battery_percentage > 100:
            self.battery_percentage = 100
        print(f"Charging... Battery is now at {self.battery_percentage}%")
    
    # Method to show smartphone details
    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery Percentage: {self.battery_percentage}%")

# Inheritance example
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_percentage, camera_quality):
        # Initialize parent class attributes
        super().__init__(brand, model, battery_percentage)
        self.camera_quality = camera_quality
    
    # Overriding the show_details method to include camera details
    def show_details(self):
        super().show_details()  # Call the parent method
        print(f"Camera Quality: {self.camera_quality}")

# Example usage:
phone1 = Smartphone("Apple", "iPhone 14", 75)
phone1.make_call("123-456-7890")
phone1.charge(15)
phone1.show_details()

phone2 = SmartphoneWithCamera("Samsung", "Galaxy S22", 80, "108MP")
phone2.show_details()
