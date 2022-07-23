# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно
# взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


STARTING_AMOUNT = 2021
MAX_MOVE = 28

typesGame = {1: "Игра против человека",
             2: "Игра против бота", 3: "Игра против умного бота"}

while True:
    print("Выберите тип игры:")
    for t in typesGame:
        print(f"{t} - {typesGame[t]}")
    try:
        typeGame = int(input("Ваш выбор: "))
        if typeGame not in typesGame:
            raise
    except:
        print("Недопустимое значение. Повторите выбор.")
    else:
        break

print(f"Выбрана {typesGame[typeGame]}")

amount = STARTING_AMOUNT
whoseMove = randint(0, 1)
numberMove = 0
while amount > 0:
    numberMove += 1
    if whoseMove == 0:
        print("Ход игрока 1")