from datetime import datetime

class Person:
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education
    @property
    def age(self):
        day = int(self.__birth_date.split(".")[0])
        month = int(self.__birth_date.split(".")[1])
        year = int(self.__birth_date.split(".")[2])
        birth_year = datetime(year, month, day) #почему в такой последовательности аааааааааа
        if (datetime.now().month, datetime.now().day) < (birth_year.month, birth_year.day):
            return datetime.now().year - birth_year.year - 1
        else:
            return datetime.now().year - birth_year.year
    @property
    def occupation(self):
        return self.__occupation
    @property
    def higher_education(self):
        return self.__higher_education
    def introduce(self):
        print(f"{self.name} is my name.",end=" ")
        print(f"I was born on {self.__birth_date}.",end=" ")
        print(f"{self.occupation} is my occupation.",end=" ")
        if self.higher_education:
            print("I do have a higher education.",end=" ")
        else:
            print("I do not have a higher education.",end=" ")

class Classmate(Person):
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool, group_name: str):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name
    def introduce(self):
        super().introduce()
        print(f'My group is {self.group_name}.',end=" ")

class Friend(Person):
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool, hobby: str):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
    def introduce(self):
        super().introduce()
        print(f'My hobby is {self.hobby}.',end=" ")

class BestFriend(Friend):
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool, hobby: str, shared_memory: str):
        super().__init__(name, birth_date, occupation, higher_education,hobby)
        self.shared_memory = shared_memory
    def introduce(self):
        super().introduce()
        print(f'Our shared memory is {self.shared_memory}.',end=" ")

class Factory:
    types = {
        "person": Person,
        "bestFriend": BestFriend,
        "friend": Friend,
        "classmate": Classmate
    }
    def create(self, obj, **kwargs):
        return self.types[obj](**kwargs)


factory = Factory()
classmate1 = factory.create(obj = "classmate",name = "Harry", birth_date = "19.01.1993", occupation = "teacher", higher_education = False, group_name = "A1")
# print(classmate1.age) тест работы age
classmate2 = factory.create(obj = "classmate",name = "Hermione", birth_date ="23.01.2001", occupation = "student", higher_education =False, group_name = "A2")
friend1 = factory.create(obj="friend",name="Gabe",birth_date="23.06.1995",occupation="Gamer",higher_education=True,hobby="Games")
friend2 = factory.create(obj="friend",name="David",birth_date="26.07.1999",occupation="Preacher",higher_education=True,hobby="dancing :)")
person1 = factory.create(obj="person",name="Oliver",birth_date="19.01.1983",occupation="IT",higher_education=True)
person2 = factory.create(obj="person",name="Alice",birth_date="15.06.2013",occupation="child",higher_education=False)
for i in [classmate1, classmate2, friend1, friend2, person1, person2]:
    i.introduce()
    print("\n")
bfriend = factory.create(obj="bestFriend",name="Artem",birth_date="23.06.2004",occupation="Gamer",higher_education=True,hobby="Games",shared_memory="cs2")
bfriend.introduce()