try:
    age = int(input("Введите ваш возраст: "))
except ValueError:
    print("Введено не число")
else:
    if not(1 <= age <= 99):
        print("Введено неверное число")
        exit(1)

    if 11 <= age <= 14:
        print(f"Вам {age} лет")
    elif age % 10 == 1:
        print(f"Вам {age} год")
    elif 2 <= age % 10 <= 4:
        print(f"Вам {age} года")
    else:
        print(f"Вам {age} лет")