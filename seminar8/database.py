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


def GetDepartmentID(database, department):
    if department in [n[0] for n in database["departments"].values()]:
        for k, v in database["departments"].items():
            if department == v[0]:
                return k
    else:
        return None


def AddDepartment(database, department):
    departmentID = GetDepartmentID(database, department)
    if departmentID is None:
        if len(database["departments"]) == 0:
            departmentID = 1
        else:
            departmentID = max(database["departments"].keys())+1
        database["departments"][departmentID] = [department]
    return departmentID


def GetAllDepartments(database):
    return [(id, node[0]) for id, node in database["departments"].items()]


def GetPositionstID(database, position):
    if position in [n[0] for n in database["positions"].values()]:
        for k, v in database["positions"].items():
            if position == v[0]:
                return k
    else:
        return None


def AddPosition(database, position):
    positionID = GetPositionstID(database, position)
    if positionID is None:
        if len(database["positions"]) == 0:
            positionID = 1
        else:
            positionID = max(database["positions"].keys())+1
        database["positions"][positionID] = [position]
    return positionID


def GetAllPositions(database):
    return [(id, node[0]) for id, node in database["positions"].items()]


def AddPerson(database, name, tel, department, position):
    departmentID = AddDepartment(database, department)
    positionID = AddPosition(database, position)
    if len(database["persons"]) == 0:
        personID = 1
    else:
        personID = max(database["persons"].keys())+1
    database["persons"][personID] = [name, tel, departmentID, positionID]


def GetPerson(database, id):
    if id in database["persons"]:
        return (
            id,
            database["persons"][id][0],
            database["persons"][id][1],
            database["departments"][database["persons"][id][2]][0],
            database["positions"][database["persons"][id][3]][0]
        )
    else:
        return None


def GetAllPersons(database):
    return [GetPerson(database, key) for key in database["persons"].keys()]


def GetFilterPersonID(database, search):
    return [k for k, v in database["persons"].items() if search.lower() in v[0].lower()]

def GetFilterPerson(database, search):
    return [GetPerson(database, k) for k, v in database["persons"].items() if search.lower() in v[0].lower()]


def RemovePerson(database, id):
    database["persons"].pop(id, None)


if __name__ == "__main__":
    db = OpenDataBase()
    # AddPerson(db, "Иванов", "111111111", "Снабжение", "Специалист по закупкам")
    # AddPerson(db, "Петров", "2222222", "Охрана", "Сесюрити")
    # AddPerson(db, "Сидоров", "4568477", "Снабжение", "Руководитель")
    # AddPerson(db, "Иванков", "976865455", "Ай Ти", "Программист")
    print(GetAllDepartments(db))
    print()
    print(GetAllPositions(db))
    print()
    print(GetAllPersons(db))
    print()

    print(GetFilterPersonID(db, "Иван"))
    print(GetFilterPerson(db, "Иван"))

    # RemovePerson(db, 55)
    # print()
    # filter = FilterPerson(db, "Иван")
    # for id in filter:
    #     print(GetPerson(db, id))
    # SaveDataBase(db)
    # print(db)
