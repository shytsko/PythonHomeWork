# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

inputList = ["qwe", "asd", "234", "zxc", "qwe",
             "ertqwe", "123", "ячс", "фыв", "567"]

# inputList = ["qwe", "asd", "zxc", "qwe", "ertqwe", "ячс", "фыв"]


def FindNumber(input: list):
    output = []
    for item in input:
        if item.isdigit():
            output.append(item)
    return output


outputList = FindNumber(inputList)
print(f"Список {inputList}", end=" ")
if len(outputList) > 0:
    print(f"содержит числа {' '.join(outputList)}")
else:
    print("не содержит чисел")
