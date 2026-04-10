class Animal:
    def __init__(self):
        self.__age = 0
        self.__name = ""
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        self.__age = value
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    def make_sound(self):
        print("Animal made a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog made a sound")

class Cat(Animal):
    def make_sound(self):
        print("Cat made a sound")

animal = Animal()
animal.make_sound()
dog = Dog()
dog.make_sound()
cat = Cat()
cat.make_sound()
animal.age = 5
animal.name = "CREATURE"
print(f"{animal.name} is {animal.age} years old")
dog.age = 3
dog.name = "Bobik"
print(f"{dog.name} is {dog.age} years old")
cat.age = 12
cat.name = "Tessa"
print(f"{cat.name} is {cat.age} years old")
