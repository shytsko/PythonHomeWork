from ui import *
from database import *


def run():
    actions = [
        "Показать все записи",
        "Добавить запись",
        "Удалить запись",
        "Фильтр",
        "Показать справочник отделов",
        "Показать справочник должностей",
        "Сохранить"
    ]

    db = OpenDataBase()

    while True:
        action = Menu(actions)
        if action is None:
            return
        match action:
            case "Показать все записи":
                ShowAndChoiceData(GetAllPersons(db), "Все записи")
            case "Добавить запись":
                newData = InputData()
                if newData is not None:
                    AddPerson(db, newData[0], newData[1],
                              newData[2], newData[3])
            case "Удалить запись":
                id = GetRemoveID(GetAllPersons(db))
                RemovePerson(db, id)
            case "Фильтр":
                filterValue = GetFilterValue()
                if filterValue is not None:
                    ShowAndChoiceData(GetFilterPerson(db, filterValue), f"Отфильтрованные записи по '{filterValue}'")
            case "Показать справочник отделов":
                Showdirectory(GetAllDepartments(db), "Справочник отделов")
            case "Показать справочник должностей":
                Showdirectory(GetAllPositions(db), "Справочник должностей")
            case "Сохранить":
                SaveDataBase(db)
            case _:
                print(action)

