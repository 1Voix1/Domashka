try:
    a = float(input("Введите первое число (a): "))
    b = float(input("Введите второе число (b): "))
    c = float(input("Введите третье число (c): "))
except ValueError:
    print("Введено не число")
else:
    print(f"Минимальное: {min(a,b,c)}", f"Максимальное: {max(a,b,c)}", sep="\n")