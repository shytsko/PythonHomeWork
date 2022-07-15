# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.

# Sample Input 1: a aa abC aa ac abc bcd a
# Sample Output 1:
# ac 1
# a 2
# abc 2
# bcd 1
# aa 2

# Sample Input 2: a A a
# Sample Output 2:
# a 3

testInput = ["a aa abC aa ac abc bcd a", "a A a"]

def CountWords(text: str) -> dict:
    result = {}
    wordList = text.lower().split()
    for word in wordList:
        if word in result.keys():
            result[word] += 1
        else:
            result[word] = 1
    return result

for _ in testInput:
    print(f"Входная строка: {_}")
    countWords = CountWords(_)
    for word, count in countWords.items():
        print(f"{word} - {count}")
