try:
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
except ValueError:
    print("Введено не число")
else:
    is_in_circle = x**2 + y**2 <= 1
    is_on_left_side = x <= 0
    is_above_line = y>=x
    if(is_in_circle and is_on_left_side) or (is_in_circle and is_above_line):
        print(f"Точка ({x}; {y}) принадлежит закрашенной области")
    else:
        print(f"Точка ({x}; {y}) НЕ принадлежит закрашенной области")