# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов. Это не просто сумма всех коэффициентов.
# Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.
# например, в 1 файле было 3*x^3 + 5*x^2+10*x+11, в другом 7*x^2+55 то в итоге будет, 3*x^3 + 12*x^2+10*x+66


def GenerateTerms(coef: int, pow: int) -> str:
    if pow == 0:
        return f"{coef}"
    elif pow == 1:
        return f"{coef}*x"
    else:
        return f"{coef}*x^{pow}"


def DecodePolynome(polyStr: str) -> dict:
    listTerms = polyStr.split(" = ")[0].split(" + ")
    dicrTerms = {}
    for term in listTerms:
        if "^" in term:
            tmp = term.split("^")
            dicrTerms[int(tmp[1])] = int(tmp[0].split("*")[0])
        elif "*" in term:
            dicrTerms[1] = int(term.split("*")[0])
        else:
            dicrTerms[0] = int(term)
    return dicrTerms


def EncodePolynome(polyDict: dict) -> str:
    pow = list(polyDict.keys())
    pow.sort()
    pow.reverse()
    terms = []
    for p in pow:
        terms.append(GenerateTerms(polyDict[p], p))
    return " + ".join(terms) + " = 0"


def SumPolynome(poly1: dict, poly2: dict) -> dict:
    pow = set(poly1.keys()) | set(poly2.keys())
    result = {}
    for p in pow:
        result[p] = (poly1[p] if p in poly1 else 0) + \
            (poly2[p] if p in poly2 else 0)
    return result


try:
    with open(r"seminar5\polynom1.txt", "r") as f:
        polyStr1 = f.readline()
    with open(r"seminar5\polynom2.txt", "r") as f:
        polyStr2 = f.readline()
except:
    print("Не удалось загрузить файл")
    exit()

print(polyStr1)
print(polyStr2)
polynom1 = DecodePolynome(polyStr1)
polynom2 = DecodePolynome(polyStr2)
sumPolynome = SumPolynome(polynom1, polynom2)
sumPolyStr = EncodePolynome(sumPolynome)
print(sumPolyStr)

try:
    with open(r"seminar5\sumpolynom.txt", "w") as f:
        f.write(sumPolyStr)
except:
    print("Не удалось записать файл")
    exit()