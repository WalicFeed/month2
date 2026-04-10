class Animal:
    def move(self):
        print("animal moved")

class Swimming(Animal):
    def move(self):
        super().move()
        print("swimming animal")

class Flying(Animal):
    def move(self):
        print("flying animal")

class Duck(Swimming, Flying):
    def move(self):
        super().move()
        print("duck moved")

duck = Duck()
duck.move()
