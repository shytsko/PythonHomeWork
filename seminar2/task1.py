# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11


try:
    number = float(input("Введите вещественное число: "))
except:
    print("Нужно было ввести вещественное число!")
    exit()


def SumDigits(n):
    digits = int(str(n).replace('.', ''))

    sum = 0
    while digits != 0:
        sum += digits % 10
        digits //= 10
    return sum

print(SumDigits(number))
