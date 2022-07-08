# **Задача 1.** Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет
try:
    dayNumber = int(input('Введите день недели: '))
except:
    print('Нужно было ввести целое число!')
    exit()


def IsDayOff(dayNumber):
    return dayNumber == 6 or dayNumber == 7

def IsWorkingDay(dayNumber):
    return 1 <= dayNumber <= 5
        

if IsDayOff(dayNumber):
    print('Выходной.')
elif IsWorkingDay(dayNumber):
    print('Не выходной.')
else:
    print('Нет такого дня недели.')
