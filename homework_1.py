
class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduse(self):
        if self.higher_education:
            edu_text = "есть"
        else:
            edu_text = "нет"
        print(f"Привет. Меня зовут {self.name}. Я родился {self.birth_date}. По профисии {self.occupation}. Высшего образование {edu_text}")


person_1 = Person(name = "Айзат", birth_date = "24.06.2006", occupation = "студент", higher_education = True)
person_2 = Person(name = "Роза", birth_date = "05.11.2003", occupation = "учитель математики", higher_education = True)
person_3 = Person(name = "Ратбек", birth_date = "15.03.2011", occupation = "школьник", higher_education = False)
print(f"Name = {person_1.name}, birth_date = {person_1.birth_date}, occupation = {person_1.occupation} , higher_education = {person_1.higher_education} ")
print(f"Name = {person_2.name}, birth_date = {person_2.birth_date}, occupation = {person_2.occupation} , higher_education = {person_2.higher_education} ")
print(f"Name = {person_3.name}, birth_date = {person_3.birth_date}, occupation = {person_3.occupation} , higher_education = {person_3.higher_education} ")

person_1.introduse()
person_2.introduse()
person_3.introduse()

