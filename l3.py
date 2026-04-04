class Car:
    def __init__(self, color, horse_power):
        self.color = color
        self.horse_power = horse_power
        self.__max_speed = 120 #private
    def _check_fuel(self):
        return True #только для юзания внутри класса
    def __test(self):
        self.__max_speed = 90
        print(f"Max speed:  {self.__max_speed} due to jackasses")
    def drive_to(self, destination):
        if self._check_fuel():
            print("There is enough fuel to drive")
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

car1 = Car("red", 100)
# print(car1.__max_speed)
print(car1._Car__max_speed) #pipyava
#@Abstractmethod