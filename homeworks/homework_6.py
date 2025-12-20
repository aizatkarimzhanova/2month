from blessed import Terminal

term = Terminal()

print(term.red("apple 🍎"))
print(term.olivedrab("banana 🍌"))
print(term.yellow("cherry 🍒"))
print(term.teal("grape 🍇"))
print(term.purple1("mango 🥭"))
print(term.slategray3("orange 🍊"))
print(term.gray46("peach 🍑"))

from homework_1 import Person

person_1 = Person(name = "Айзат", birth_date = "24.06.2006", occupation = "студент", higher_education = True)
person_2 = Person("Роза", "05.11.2003", "учитель математики", True)
print(f"Name = {person_1.name}, birth_date = {person_1.birth_date}, occupation = {person_1.occupation} , higher_education = {person_1.higher_education} ")
print(f"Name = {person_2.name}, birth_date = {person_2.birth_date}, occupation = {person_2.occupation} , higher_education = {person_2.higher_education} ")

person_1.introduse()
person_2.introduse()




