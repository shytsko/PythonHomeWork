# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7] => [1, 5]

def GetRange(data: list) -> list:
    minValue = min(data)
    maxValue = max(data)
    items = set(data)
    if len(items) == maxValue-minValue+1:
        return [(minValue, maxValue)]
    else:
        result = []
        notItems = list({n for n in range(minValue, maxValue)} - items)
        notItems.sort()
        for a in notItems:
            sequence = {n for n in items if n < a}
            if len(sequence) > 1:
                result.append((min(sequence), max(sequence)))
            items = items - sequence
        return result


test1 = [1, 5, 2, 3, 4, 6, 1, 7]
test2 = [1, 5, 2, 3, 4, 1, 7]
test3 = [1, 5, 2, 3, 4, 1, 7, 8, 9, 11, 15, 20, 16, 18, 17, 23, 21]
print(test1, end=" -> ")
print(GetRange(test1))
print(test2, end=" -> ")
print(GetRange(test2))
print(test3, end=" -> ")
print(GetRange(test3))
