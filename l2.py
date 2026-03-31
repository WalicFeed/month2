class Car:
    def __init__(self, color, horse_power):
        self.color = color
        self.horse_power = horse_power
    def drive_to(self, destination):
        # self.set_color("black") можно вызывать из верхней нижнюю
        print(f"Car colored {self.color} is driving to {destination}")
    def set_color(self, color):
        self.color = color

class Bus(Car):
    def __init__(self, color, horse_power, capacity):
        super().__init__(color, horse_power)
        self.capacity = capacity
    def drive_to(self, destination):
        # super().drive_to(destination)
        print(f"Bus colored {self.color} is driving to {destination}")
    def set_color(self, color):
        self.color = color
        print(f"I am {self.color}")

class Track(Car):
    def __init__(self, color, horse_power, weight):
        super().__init__(color, horse_power)
        self.weight = weight
    def weight(self, update):
        self.weight += update
    def get_weight(self):
        return self.weight

new_bus = Bus("red", "blue", 56)
new_bus.drive_to("home")
new_bus.set_color("blue")