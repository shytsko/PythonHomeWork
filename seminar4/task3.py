# 3. (необязательное). Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
# Sample Input:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6


def NewTeam() -> dict:
    return {"matches": 0, "wins": 0, "draws": 0, "losses": 0, "goals": 0}
teams = {}

try:
     with open("seminar4\\task3input.txt", "r", encoding="utf-8") as inputFile:
        countMatches = int(inputFile.readline())
        for line in inputFile.read().split("\n"):
            team1, goals1, team2, goals2 = line.split(";")
            goals1 = int(goals1)
            goals2 = int(goals2)
            if(team1 not in teams):
                teams[team1] = NewTeam()
            if(team2 not in teams):
                teams[team2] = NewTeam()
            teams[team1]["matches"] += 1
            teams[team2]["matches"] += 1
            teams[team1]["goals"] += goals1
            teams[team2]["goals"] += goals2
            if goals1 > goals2:
                teams[team1]["wins"] += 1
                teams[team2]["losses"] += 1
            elif goals1 < goals2:
                teams[team1]["losses"] += 1
                teams[team2]["wins"] += 1
            else:
                teams[team1]["draws"] += 1
                teams[team2]["draws"] += 1
except:
    print("Не удалось прочитать файл")
    exit()
else:
    print("Файл успешно прочитан")

try:
    with open("seminar4\\task3output.txt", "w", encoding="utf-8") as outputFile:
        for team in teams.keys():
            outputFile.write(
                f"{team}:{teams[team]['matches']} {teams[team]['wins']} {teams[team]['draws']} {teams[team]['losses']} {teams[team]['goals']}\n")
except:
    print("Не удалось записать файл")
    exit()
else:
    print("Файл успешно записан")
