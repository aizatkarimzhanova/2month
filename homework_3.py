class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        if self.higher_education:
            edu_text = "есть"
        else:
            edu_text = "нет"
        print(f"""Привет. Меня зовут {self.name}. Я родился {self.birth_date}. По профисии {self.occupation}. Высшего образование {edu_text}""")

class Classmate(Person):
    # добавление новых атрибутов
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        edu_text = "есть" if self.higher_education else "нет"
        print(f"""Привет, меня зовут {self.name}, я одноклассница Айзат. 
Родился {self.birth_date}. Профессия — {self.occupation}. 
Высшее образование {edu_text}.""")
        print(f"Мы с Айзат учились в {self.group_name} классе.")

class Friend(Person):
    # добавление новых атрибутов
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
        
    def introduce(self):
        edu_text = "есть" if self.higher_education else "нет"
        print(f"""Привет, меня зовут {self.name}, я подруга Айзата. 
Родился {self.birth_date}. Профессия — {self.occupation}. 
Высшее образование {edu_text}.""")
        print(f"Моё хобби — {self.hobby}")
        
person = Person("Айзат", "24.06.2006", "студент", True)
person_1 = Classmate("Диана", "05.06.2005", "студент", True, "5-A")
person_2 = Classmate("Нурзат", "03.08.2006", "студент", True, "5-A")
person_3 = Friend("Роза", "05.11.2003", "учитель математики", True, "рисование")
person_4 = Friend("Умутай", "27.09.2005", "повар", False, "читать книги")

person.introduce()
person_1.introduce()
person_2.introduce()
person_3.introduce()
person_4.introduce()
