# открыть базу (она же считает из файла)+
# закрыть базу (запишет в файл)+
# найти записи (выдаст наверх стоку вида id-фамилия-должность-отдел или в другом виде, но сама в консоль ничего выводить не будет)
# удалить запись (по id сотрудника)
# добавить запись (фамилия, телефон, должность, отдел) - должность и отдел будут задаваться текстом, но внутри будет проверка
# на наличие таких среди уже имеющихся+
# выдать список имеющихся отделов
# выдать список имеющихся должностей

import json


# db = {
#     "persons": {
#         1: ["Иванов", "6456465", 2, 2],
#         2: ["Петров", "654654", 1, 1],
#         3: ["Сидоров", "56564645", 3, 3]
#     },
#     "departments": {
#         1: ["ПТО"],
#         2: ["Бухгалтерия"],
#         3: ["Снабжение"]
#     },
#     "positions": {
#         1: ["Руководитель"],
#         2: ["Специалист"],
#         3: ["Инженер"]
#     }
# }


def OpenDataBase():
    try:
        with open("directory.json", "r", encoding="utf-8") as fh:
            db = json.load(fh)
            db["persons"] = {int(k): v for k, v in db["persons"].items()}
            db["departments"] = {
                int(k): v for k, v in db["departments"].items()}
            db["positions"] = {int(k): v for k, v in db["positions"].items()}
            return db
    except:
        return {"persons": {}, "departments": {}, "positions": {}}


def SaveDataBase(directory):
    with open("directory.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(directory, ensure_ascii=False))


def AddPerson(database, name, tel, department, position):
    if department in [n[0] for n in database["departments"].values()]:
        for k, v in database["departments"].items():
            if department == v[0]:
                departmentID = k
                break
    else:
        if len(database["departments"]) == 0:
            departmentID = 1
        else:
            departmentID = max(database["departments"].keys())+1
        database["departments"][departmentID] = [department]

    if position in [n[0] for n in database["positions"].values()]:
        for k, v in database["positions"].items():
            if position == v[0]:
                positionID = k
                break
    else:
        if len(database["positions"]) == 0:
            positionID = 1
        else:
            positionID = max(database["positions"].keys())+1
        database["positions"][positionID] = [position]

    if len(database["persons"]) == 0:
        personID = 1
    else:
        personID = max(database["persons"].keys())+1
    database["persons"][personID] = [name, tel, departmentID, positionID]


if __name__ == "__main__":
    db = OpenDataBase()
    AddPerson(db, "Иванов", "111111111", "Снабжение", "Специалист по закупкам")
    AddPerson(db, "Петров", "2222222", "Охрана", "Сесюрити")
    AddPerson(db, "Сидоров", "4568477", "Снабжение", "Руководитель")
    AddPerson(db, "Пупкин", "976865455", "Охрана", "Руководитель")
    SaveDataBase(db)
    print(db)

