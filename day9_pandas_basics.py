import pandas as pd

data = {
    "name": ["Иван", "Мария", "Пётр", "Дмитрий", "Владимир"],
    "age": [16, 15, 17, 14, 13],
    "grade": [85, 92, 78, 77, 90]
}

df = pd.DataFrame(data)
print(df)

good_students = df[df["grade"] > 85]
print(good_students)

print(df["grade"].mean())

print(df.sort_values("grade", ascending = False))
