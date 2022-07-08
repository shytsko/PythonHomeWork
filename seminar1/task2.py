# **Задача 3.** Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

try:
    x = float(input('Введите координату x: '))
    y = float(input('Введите координату y: '))
except:
    print('Нужно ввести число!')
    exit()


def GetQuarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return 0


def GetAxis(x, y):
    if x == 0 and y == 0:
        return 'X и Y'
    elif x == 0:
        return 'Y'
    elif y == 0:
        return 'X'
    else:
        return ''


quart = GetQuarter(x, y)
if quart != 0:
    print(f'Точка ({x}, {y}) находится в четверти {quart}')
else:
    print(f'Точка ({x}, {y}) находится на оси {GetAxis(x, y)}')
