# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно
# взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


startirngAmount = 521
maxMove = 28

typesGame = {1: "Игра против человека",
             2: "Игра против бота"}


def GetGameType() -> int:
    while True:
        print("Выберите тип игры:")
        for t in typesGame:
            print(f"{t} - {typesGame[t]}")
        try:
            type = int(input("Ваш выбор: "))
            if type not in typesGame:
                raise
        except:
            print("Недопустимое значение. Повторите выбор.")
        else:
            return type


def GetHumanMove(amount: int) -> int:
    global maxMove
    while True:
        try:
            count = int(input("Сколько конфет нужно забрать: "))
            if count < 1 or count > min(amount, maxMove):
                raise
        except:
            print("Недопустимое значение. Повторите ввод.")
        else:
            return count


def GetBotMove(amount: int) -> int:
    global maxMove
    move = amount % (maxMove + 1) if amount % (maxMove + 1) != 0 else 1
    print(f"Бот забрал конфет: {move}")
    return move


gameType = GetGameType()
print(f"Выбрана {typesGame[gameType]}")

amount = startirngAmount
whoseMove = randint(0, 1)
if whoseMove == 1:
    print("Вы ходите первым")
else:
    print("Ваш противник ходит первым")
while amount > 0:
    print("----------------------------")
    print(f"Конфет осталось: {amount}")
    whoseMove = (whoseMove + 1) % 2
    if whoseMove == 0:
        print("Ваш ход.")
        move = GetHumanMove(amount)
    else:
        print("Ход противника")
        move = GetHumanMove(amount) if gameType == 1 else GetBotMove(amount)
    amount -= move

print("Конфет больше не осталось.")
if whoseMove == 0:
    print("Вы победили!!!")
else:
    print("Противник победил!!!")
