class Person:
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        print(f"{self.name} is my name\n")
        print(f"I was born on {self.birth_date}.\n")
        print(f"{self.occupation} is my occupation\n")
        if self.higher_education:
            print("I do have a higher education\n\n")
        else:
            print("I do not have a higher education\n\n")

class Classmate(Person):
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool, group_name: str):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name
    def introduce(self):
        super().introduce()
        print(f'My group is {self.group_name}\n')

class Friend(Person):
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool, hobby: str):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
    def introduce(self):
        super().introduce()
        print(f'My hobby is {self.hobby}\n')

classmate1 = Classmate("Harry", "19.01.1993", "teacher", False, "A1")
classmate2 = Classmate("Hermione", "23.01.2001", "student", False, "A2")
friend1 = Friend("Gabe", "23.06.1995", "Gamer", True, "Games")
friend2 = Friend("David", "67.31.1999", "Preacher", True, "children")