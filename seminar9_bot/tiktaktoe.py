# 1. Создайте программу для игры в "Крестики-нолики".
import random

EPMTY = 0
X = 1
O = -1
SYMBOLS = {EPMTY: "-", X: "X", O: "O"}

X_WIN = X
O_WIN = O
DRAW = 0
NOT_END = -2
OCCUPIED = -3
ILLEGAL_MOVE = -4


def CheckBoard(brd):
    winCombinationX = (X, X, X)
    winCombinationO = (O, O, O)
    combinations = tuple(map(tuple, [brd[0:3], brd[3:6], brd[6:9],
                                     brd[0:9:3], brd[1:9:3], brd[2:9:3],
                                     brd[0:9:4], brd[-3:-8:-2]]))
    if winCombinationX in combinations:
        return X_WIN
    elif winCombinationO in combinations:
        return O_WIN
    elif EPMTY in brd:
        return NOT_END
    else:
        return DRAW


def NewBoard():
    return [EPMTY, EPMTY, EPMTY,
            EPMTY, EPMTY, EPMTY,
            EPMTY, EPMTY, EPMTY]


def PrintBoard(brd: list):
    return (" ".join(map(lambda i: SYMBOLS[i], brd[0:3])) + "\n" +
            " ".join(map(lambda i: SYMBOLS[i], brd[3:6])) + "\n" +
            " ".join(map(lambda i: SYMBOLS[i], brd[6:9])) + "\n")


def MoveAndCheck(brd: list, move: int, wMove: int):
    if move not in range(len(brd)):
        return ILLEGAL_MOVE
    if brd[move] != EPMTY:
        return OCCUPIED
    brd[move] = wMove
    return CheckBoard(brd)


def InputHumanMove():
    while True:
        try:
            m = input("Сделайте ход (строка столбец через пробел): ")
            i, j = list(map(int, m.split()))
            move = (i-1)*3 + (j-1)
        except:
            print("Ошибка")
        else:
            return move


def _OneMoveWin(brd: list, moves: set, wMove: int) -> int:
    for move in moves:
        newBrd = brd[::]
        newBrd[move] = wMove
        if CheckBoard(newBrd) == wMove:
            return move
    return -1


def _TwoMoveWin(brd: list, priorityMoves: set, allMoves: set, wMove: int) -> int:
    for firstMove in priorityMoves:
        newBrd = brd[::]
        newBrd[firstMove] = wMove
        for secondMove in allMoves - {firstMove}:
            newBrdSecond = newBrd[::]
            newBrdSecond[secondMove] = wMove
            if CheckBoard(newBrdSecond) == wMove:
                return firstMove
    return -1


def BotMove(brd: list, wMove: int):
    possibleMoves = {m for m, s in enumerate(brd) if s == EPMTY}
    cornerСellsEmpty = possibleMoves & {0, 2, 6, 8}
    sideСellsEmpty = possibleMoves & {1, 3, 5, 7}
    center = 4
    opponent = X if wMove == O else O
    move = _OneMoveWin(brd, possibleMoves, wMove)
    if move != -1:
        return move
    move = _OneMoveWin(brd, possibleMoves, opponent)
    if move != -1:
        return move
    if brd[center] == EPMTY:
        return center
    else:
        if len(cornerСellsEmpty) == 2 and ((brd[0] == opponent and brd[8] == opponent) or (brd[2] == opponent and brd[6] == opponent)):
            move = _TwoMoveWin(brd, sideСellsEmpty, possibleMoves, wMove)
            if move != -1:
                return move
    move = _TwoMoveWin(brd, cornerСellsEmpty, possibleMoves, wMove)
    if move != -1:
        return move
    move = _TwoMoveWin(brd, possibleMoves, possibleMoves, wMove)
    if move != -1:
        return move
    if len(cornerСellsEmpty) != 0:
        return random.choice(tuple(cornerСellsEmpty))
    return random.choice(tuple(possibleMoves))


if __name__ == "__main__":
    board = NewBoard()

    whoseMove = random.randint(0, 1)
    if whoseMove != X:
        print("Первым ходит X")
    else:
        print("Первым ходит O")
    gameState = NOT_END
    print(PrintBoard(board))
    while gameState not in (X_WIN, O_WIN, DRAW):
        if gameState == NOT_END:
            whoseMove = (whoseMove + 1) % 2
        if whoseMove == X:
            print("Ход X")
            # move = InputHumanMove()
            move = BotMove(board, X)
            gameState = MoveAndCheck(board, move, X)
        else:
            print("Ход O")
            move = BotMove(board, O)
            gameState = MoveAndCheck(board, move, O)
        if gameState == OCCUPIED:
            print("Ячейка занята. Повторите ход")
        elif gameState == ILLEGAL_MOVE:
            print("Не верный ход. Повторите")
        print(PrintBoard(board))
        print("-----------------")

    if gameState == X_WIN:
        print("X победил!!!")
    elif gameState == O_WIN:
        print("O победил!!!")
    else:
        print("Ничья!!!")
