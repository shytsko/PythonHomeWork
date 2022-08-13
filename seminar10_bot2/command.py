from telegram import Update, ParseMode
from telegram.ext import CallbackContext, ConversationHandler
from database import *
import logging

_db = None
_newName = ""
_newTel = ""
_newDepartment = ""
_newPosition = ""
_id = 0

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

SELECT, INPUTNAME, INPUTTEL, INPUTDEP, INPUTPOS, INPUTFILTER, INPUTID, CONFIRMREM = range(
    8)


def SendMenu(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Выберите действие:\n"
        "/viewall - Показать все записи\n"
        "/filter - Показать записи по фильтру\n"
        "/add - Добавить запись\n"
        "/remove - Удалить запись\n"
        "/departments - Показать справочник отделов\n"
        "/positions - Показать справочник должностей\n"
        "/save - сохранить изменения\n"
        "/done - завершить работу"
    )


def start(update: Update, context: CallbackContext) -> int:
    global _db
    user = update.message.from_user
    logger.info(f"Пользователь {user.first_name} начал работу с базой")
    _db = OpenDataBase()
    SendMenu(update, context)
    return SELECT


def ViewAll(update: Update, context: CallbackContext) -> int:
    global _db
    user = update.message.from_user
    logger.info(f"Пользователь {user.first_name} выбрал просмотр всей базы")
    data = GetAllPersons(_db)
    message = "\n".join(
        [f"{item[0]}, {item[1]}, {item[2]}, {item[3]}, {item[4]}" for item in data])
    update.message.reply_text(message)
    SendMenu(update, context)
    return SELECT


def AddItem(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(f"Пользователь {user.first_name} выбрал добавление записи")
    update.message.reply_text("Введите имя сотрудника или /cancel для отмены.")
    return INPUTNAME


def InputName(update: Update, context: CallbackContext) -> int:
    global _newName
    user = update.message.from_user
    text = update.message.text
    logger.info(f"Пользователь {user.first_name} ввел имя сотрудника '{text}'")
    _newName = text
    update.message.reply_text(
        "Введите телефон сотрудника или /cancel для отмены.")
    return INPUTTEL


def InputTel(update: Update, context: CallbackContext) -> int:
    global _newTel
    user = update.message.from_user
    text = update.message.text
    logger.info(
        f"Пользователь {user.first_name} ввел телефон сотрудника '{text}'")
    _newTel = text
    update.message.reply_text(
        "Введите название отдела или /cancel для отмены.")
    return INPUTDEP


def InputDepartment(update: Update, context: CallbackContext) -> int:
    global _newDepartment
    user = update.message.from_user
    text = update.message.text
    logger.info(
        f"Пользователь {user.first_name} ввел название отдела '{text}'")
    _newDepartment = text
    update.message.reply_text(
        "Введите должность сотрудника или /cancel для отмены.")
    return INPUTPOS


def InputPosition(update: Update, context: CallbackContext) -> int:
    global _newName, _newTel, _newDepartment, _newPosition, _db
    user = update.message.from_user
    text = update.message.text
    logger.info(
        f"Пользователь {user.first_name} ввел должность сотрудника '{text}'")
    _newPosition = text
    AddPerson(_db, _newName, _newTel, _newDepartment, _newPosition)
    logger.info(
        f"Пользователь {user.first_name} добавил нового сотрудника '{_newName}, {_newTel}, {_newDepartment}, {_newPosition}'")
    _newName, _newTel, _newDepartment, _newPosition = ("", "", "", "")
    SendMenu(update, context)
    return SELECT


def CancelAdd(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(
        f"Пользователь {user.first_name} отменил добавление новой записи")
    SendMenu(update, context)
    return SELECT


def ViewFilter(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(
        f"Пользователь {user.first_name} выбрал просмотр базы по фильтру")
    update.message.reply_text("Введите строку для фильтрации.")
    return INPUTFILTER


def InputFilter(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    text = update.message.text
    logger.info(
        f"Пользователь {user.first_name} ввел строку для фильрации '{text}'")
    data = GetFilterPerson(_db, text)
    if len(data) != 0:
        message = "\n".join(
            [f"{item[0]}, {item[1]}, {item[2]}, {item[3]}, {item[4]}" for item in data])
    else:
        message = "Нет данных. удовледворяющих условию фильтрации."
    update.message.reply_text(message)
    SendMenu(update, context)
    return SELECT


def CancelFilter(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(
        f"Пользователь {user.first_name} отменил просмотр базы по фильтру")
    SendMenu(update, context)
    return SELECT


def RemoveItem(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(f"Пользователь {user.first_name} выбрал удаление записи")
    update.message.reply_text(
        "Введите id сотрудника для удаления или /cancel для отмены.")
    return INPUTID


def InputID(update: Update, context: CallbackContext) -> int:
    global _id
    user = update.message.from_user
    text = update.message.text
    logger.info(
        f"Пользователь {user.first_name} ввел id сотрудника для удаления '{text}'")
    try:
        _id = int(text)
        person = GetPerson(_db, _id)
        if person == None:
            raise
    except:
        update.message.reply_text(
            "Вы ввели не верный id.\nВведите id сотрудника для удаления или /cancel для отмены.")
        return INPUTID
    update.message.reply_text("Вы хотите удалить сотрудника?\n\n"
                              f"{person[0]}, {person[1]}, {person[2]}, {person[3]}, {person[4]}\n\n"
                              "Введите /confirm для подтвержденияили или /cancel для отмены")
    return CONFIRMREM


def ConfirmRemove(update: Update, context: CallbackContext) -> int:
    global _db, _id
    user = update.message.from_user
    logger.info(
        f"Пользователь {user.first_name} подтвердил удаление записи с id = {_id}")
    RemovePerson(_db, _id)
    SendMenu(update, context)
    return SELECT


def CancelRemove(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(
        f"Пользователь {user.first_name} отменил удаление записи")
    SendMenu(update, context)
    return SELECT


def ViewDepartments(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(
        f"Пользователь {user.first_name} выбрал просмотр справочника отделов")
    SendMenu(update, context)
    return SELECT


def ViewPositions(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(
        f"Пользователь {user.first_name} выбрал просмотр справочника должностей")
    SendMenu(update, context)
    return SELECT


def SaveDB(update: Update, context: CallbackContext) -> int:
    SaveDataBase(_db)
    user = update.message.from_user
    logger.info(f"Пользователь {user.first_name} сохранил базу")
    SendMenu(update, context)
    return SELECT


def Done(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(f"Пользователь {user.first_name} завершил работу с базой")
    update.message.reply_text("Работа завершена")
    return ConversationHandler.END


def text(update, context):
    user = update.message.from_user
    text_received = update.message.text
    logger.info(
        f"Пользователь {user.first_name} ввел сообщение '{update.message.text}'")


def unknown(update, context):
    user = update.message.from_user
    logger.info(
        f"Пользователь {user.first_name} ввел не обработанную комаду '{update.message.text}'")


def error(update, context):
    pass
