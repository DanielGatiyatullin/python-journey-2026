class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет")


person1 = Person("Иван", 16)
person1.introduce()

person2 = Person("Глеб", 12)
person2.introduce()