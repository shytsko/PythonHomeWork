# Вычислить число π c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}
from math import log10


def CalcPi(acc: float) -> float:
    pi = 0
    pi_prev = 1
    k = 0
    while abs(pi_prev - pi) > acc:
        pi_prev = pi
        pi += (4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6)) / (16**k)
        k += 1
    return round(pi, -int(log10(accuracy)))


try:
    accuracy = float(input("Введите точность 1e-10 до 1e-1: "))
    if (accuracy < 1e-10 or accuracy > 1e-1):
        raise
except:
    print("Неверный ввод")
else:
    print(CalcPi(accuracy))
