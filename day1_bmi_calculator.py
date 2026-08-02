weight = float(input("Сколько ты весишь (кг)? "))
height = float(input("Какой у тебя рост (м)? "))

index = weight / (height * height)

print("Твой ИМТ:", round (index, 2))

if index < 18.5:
   print("Недостаточный вес")
elif 18.5 <= index <= 24.9:
   print("Норма")
elif 25 <= index <= 29.9:
   print("Избыточный вес")
elif index >= 30:
   print("Ожирение")

   
