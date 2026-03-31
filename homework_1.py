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

person1 = Person("John", "01/04/1993", 'office_worker', True)
person1.introduce()
person2 = Person("Jorge", "11/12/2004", 'MC', False)
person2.introduce()
person3 = Person("Mike", "25/08/2003", 'freelancer', False)
person3.introduce()

#В задании указано что надо атрибуты распечатать. Вот отдельно атрибуты:
for person in [person1, person2, person3]:
    print(person.name, person.birth_date, person.occupation, person.higher_education)