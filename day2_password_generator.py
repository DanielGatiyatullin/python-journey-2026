import random

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols, ):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*"

    pool = ""
    if use_digits:
        pool = pool + digits
    if use_symbols:
        pool = pool + symbols
    if use_lowercase:
        pool = pool + lowercase
    if use_uppercase:
        pool = pool + uppercase

    password = ""
    for i in range(length):
        password = password + random.choice(pool)

    return password


# Основная часть программы
length = int(input("Какой длины должен быть пароль? "))

digits_answer = input("Включать цифры? (да/нет) ")
use_digits = (digits_answer == "да")

symbols_answer = input("Включать символы? (да/нет) ")
use_symbols = (symbols_answer == "да")

lowercase_answer = input("Включать ли строчные буквы? (да/нет) ")
use_lowercase = (lowercase_answer == "да")

uppercase_answer = input("Включать заглавные буквы? (да/нет)")
use_uppercase = (uppercase_answer == "да")





result = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
print("Твой пароль:", result)