class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
         print(f"Привет, меня зовут {self.name}, мне {self.age} лет")
ordinary_person = Person("Иван", 16) 
ordinary_person.introduce()

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
         print(f"Привет, меня зовут {self.name}, мне {self.age} лет")
ordinary_person = Person2("Глеб", 12) 
ordinary_person.introduce()

        
    