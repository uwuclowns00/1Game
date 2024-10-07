import random


def guess_number():
    number_to_guess = random.randint(1, 10)
    attempts = 3

    print("Угадай число от 1 до 10! У тебя 3 попытки.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Попытка {attempt}: Введи свое число: "))

        if guess < number_to_guess:
            print("Слишком мало!")
        elif guess > number_to_guess:
            print("Слишком много!")
        else:
            print("Поздравляю! Ты угадал число!")
            break
    else:
        print(f"Ты исчерпал попытки. Загаданное число было: {number_to_guess}")


guess_number()