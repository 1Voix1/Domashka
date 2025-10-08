try:
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
except ValueError:
    print("Введено не число")
else:
    is_in_circle = x**2 + y**2 <= 6**2
    is_in_inner_circle = x**2 + y**2 <= 3**2
    is_on_left_side = x <= 0
    is_above_zero_vertical = y >= 0
    if(is_in_circle and is_on_left_side and is_above_zero_vertical) or (is_in_circle and not is_in_inner_circle and not is_on_left_side and is_above_zero_vertical):
        print(f"Точка ({x}; {y}) принадлежит закрашенной области")
    else:
        print(f"Точка ({x}; {y}) НЕ принадлежит закрашенной области")