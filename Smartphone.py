# smartphone_class.py

# Base Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage   # in GB
        self.battery = battery   # in mAh

    # Method I have used to display phone info
    def phone_info(self):
        return f"{self.brand} {self.model} - {self.storage}GB, {self.battery}mAh"

    # Method I have used to simulate charging
    def charge(self, amount):
        self.battery += amount
        return f"Battery charged! Current capacity: {self.battery}mAh"

    # Method to I have used to install an app
    def install_app(self, app_size):
        if self.storage >= app_size:
            self.storage -= app_size
            return f"App installed! Remaining storage: {self.storage}GB"
        else:
            return "Not enough storage!"


# Subclass (Inheritance)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        # Here we call the parent constructor
        super().__init__(brand, model, storage, battery)
        self.gpu = gpu  # This is a special attribute for gaming phones

    # Polymorphism: override method
    def phone_info(self):
        return f"{self.brand} {self.model} [Gaming Edition] - {self.storage}GB, {self.battery}mAh, GPU: {self.gpu}"

    # New method for gaming
    def play_game(self, game_size, battery_usage):
        if self.storage < game_size:
            return "Not enough storage to install the game!"
        elif self.battery < battery_usage:
            return "Not enough battery to play the game!"
        else:
            self.storage -= game_size
            self.battery -= battery_usage
            return f"Played game! Remaining: {self.storage}GB, {self.battery}mAh"


# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S25", 128, 4500)
    gaming_phone = GamingSmartphone("Asus", "ROG 8", 256, 6000, "Adreno X1")

    print(phone1.phone_info())
    print(phone1.install_app(5))
    print(phone1.charge(500))

    print("\n--- Gaming Smartphone ---")
    print(gaming_phone.phone_info())
    print(gaming_phone.play_game(20, 1000))
