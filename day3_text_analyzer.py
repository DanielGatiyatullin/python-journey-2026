text = (input("Введите текст:"))
words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for key in word_count:
    print(key, "->", word_count[key])

