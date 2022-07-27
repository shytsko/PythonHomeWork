# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def RLEEncode(text: str) -> str:
    encodeText = []
    startIndex = 0
    endIndex = 1
    while startIndex < len(text):
        while endIndex < len(text) and text[startIndex] == text[endIndex]:
            endIndex += 1
        if endIndex - startIndex > 3:
            encodeText.extend(
                ["#", chr(endIndex-startIndex), text[startIndex]])
        else:
            encodeText.extend(list(text[startIndex:endIndex]))
        startIndex = endIndex
        endIndex = startIndex + 1
    return "".join(encodeText)


def RLEDecode(encodeText: str) -> str:
    decodeText = []
    startIndex = 0
    while startIndex < len(encodeText):
        if encodeText[startIndex] == "#":
            decodeText.extend([encodeText[startIndex+2]] *
                              ord(encodeText[startIndex+1]))
            startIndex += 3
        else:
            decodeText.append(encodeText[startIndex])
            startIndex += 1
    return "".join(decodeText)


try:
    with open(r"seminar6\testdata.txt", "r", encoding="utf-8") as file:
        data = file.readline()
except:
    print("Не удалось загрузить файл")
    exit()
else:
    print("Исходные данные загружены")
    print(data)
    print("-------------------------------------")

encode = RLEEncode(data)
print("Кодирование")
print(encode)
try:
    with open(r"seminar6\encodedata.txt", "w", encoding="utf-8") as file:
        file.write(encode)
except:
    print("Не удалось записать файл")
    exit()
else:
    print("Закодированные данные записаны")
    print("-------------------------------------")

try:
    with open(r"seminar6\encodedata.txt", "r", encoding="utf-8") as file:
        encodeData = file.readline()
except:
    print("Не удалось загрузить файл")
    exit()
else:
    print("Закодированные данные загружены")
    print(encodeData)
    print("-------------------------------------")

decodeData = RLEDecode(encodeData)
print("Декодирование")
print(decodeData)
try:
    with open(r"seminar6\decodedata.txt", "w", encoding="utf-8") as file:
        file.write(decodeData)
except:
    print("Не удалось записать файл")
    exit()
else:
    print("Декодированные данные записаны")
    print("-------------------------------------")
