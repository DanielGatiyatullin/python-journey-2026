import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4o")

texts = [
"Привет",
"Привет, как дела?",
"Здравствуйте! Не могли бы вы объяснить, как работает искусственный интеллект?"
]

for text in texts:
    tokens = encoding.encode(text)

print("Текст:", text)
print("Количество токенов:", len(tokens))
print("-" * 30)