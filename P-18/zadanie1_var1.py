try:
    a = float(input("Введите первое число (a): "))
    b = float(input("Введите второе число (b): "))
    c = float(input("Введите третье число (c): "))
except ValueError:
    print("Введено не число")
else:
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c

    min_num = a
    if b < min_num:
        min_num = b
    if c < min_num:
        min_num = c

    print(f"Минимальное: {min_num}", f"Максимальное: {max_num}", sep="\n")