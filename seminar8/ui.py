from easygui import *


def Menu(choices):
    msg = "Выберите действие"
    return choicebox(msg, msg, choices)


def InputData():
    msg = "Введите данные о сотруднике"
    title = "Ввод данных"
    fieldNames = ["ФИО", "Телефон", "Отдел", "Должность"]
    fieldValues = []
    fieldValues = multenterbox(msg, title, fieldNames)
    return fieldValues


def ShowAndChoiceData(data, msg):
    choices = ["id, ФИО, Телефон, Отдел, Должность", " "] + [f"{item[0]}, {item[1]}, {item[2]}, {item[3]}, {item[4]}" for item in data]
    return choicebox(msg, msg, choices)

def ShowDirectory(data, msg):
    choices = ["id, Наименование", " "] + [f"{item[0]}, {item[1]}" for item in data]
    return choicebox(msg, msg, choices)


def GetRemoveID(data):
    removeItem = ShowAndChoiceData(data, "Выберите запись для удаления")
    if removeItem is not None:
        if removeItem[0].isdigit():
            if ynbox("Вы на самом деле хотите удалить запись?\n" + removeItem):
                id = int(removeItem.split(",")[0])
                return id
    return None

def GetFilterValue():
    return enterbox("Введите критерий для фильтрации")

