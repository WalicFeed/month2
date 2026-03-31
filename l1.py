class Car:
    def __init__(self, color, horse_power):
        self.color = color
        self.horse_power = horse_power
    def drive_to(self, destination):
        # self.set_color("black") можно вызывать из верхней нижнюю
        print(f"Car colored {self.color} is driving to {destination}")
    def set_color(self, color):
        self.color = color

car1 = Car("green", 204)
car2 = Car("red", 350)
car1.drive_to("NYC")
car2.set_color("gold")
car2.model = "Subaru" #pizdez
