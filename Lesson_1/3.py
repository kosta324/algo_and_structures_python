# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.
x1 = int(input('Введите координату x1: '))
y1 = int(input('Введите координату y1: '))
x2 = int(input('Введите координату x2: '))
y2 = int(input('Введите координату y2: '))
if x1 == x2:
    print(f'согласно введенным координатам ({x1}:{y1}) & ({x2}:{y2}) '
          f'уравнение вида "y = kx + b" не существует. Результат: "x = a"')
else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1

    # на случай отрицательного значения "b" сделаем дополнительную ветку вывода
    if b < 0:
        print(f'согласно введенным координатам ({x1}:{y1}) & ({x2}:{y2}) '
              f'уравнение вида "y = kx + b" будет соответствовать:\n'
              f'y = {k:.1f}x - {b * -1:.1f}')
    elif b > 0:
        print(f'согласно введенным координатам ({x1}:{y1}) & ({x2}:{y2}) '
              f'уравнение вида "y = kx + b" будет соответствовать:\n'
              f'y = {k:.1f}x + {b:.1f}')
    else:
        print(f'согласно введенным координатам ({x1}:{y1}) & ({x2}:{y2}) '
              f'уравнение вида "y = kx + b" будет соответствовать:\n'
              f'y = {k:.1f}x')
