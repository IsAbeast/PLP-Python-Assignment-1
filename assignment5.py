class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"🔋 Charging... Battery level: {self.battery_level}%")

class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_level, cooling_system):
        super().__init__(brand, model, battery_level)  
        self.cooling_system = cooling_system

    def play_game(self, game):
        if self.battery_level > 10:
            print(f"🎮 Playing {game} on {self.brand} {self.model} with {self.cooling_system} cooling system.")
            self.battery_level -= 10
        else:
            print("❌ Battery too low to play a game!")

phone1 = Smartphone("Samsung", "S25", 50)
phone1.call("0707139073")
phone1.charge(30)

gaming_phone = GamingPhone("Redmi", "Note 14", 80, "liquid-cooling")
gaming_phone.play_game("Call of Duty Mobile")
gaming_phone.charge(15)
