class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет")
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
    def study(self):
            print(f"{self.name} учится в {self.school}")
ordinary_student = Student("Кирилл", 15, "Гимназия №5")
ordinary_student.introduce()
ordinary_student.study()