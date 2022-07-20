# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа

def GetPrimeFactors(n: int) -> list:
    result = []
    factor = 2
    while(n > 1):
        if(n % factor == 0):
            result.append(factor)
            n //= factor
        else:
            factor += 1
    return result


try:
    n = int(input("Введите натуральное число: "))
    if (n < 1):
        raise
except:
    print("Нужно вводить натуральное число")
else:
    print(GetPrimeFactors(n))
