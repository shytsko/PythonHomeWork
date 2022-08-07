from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import tiktaktoe
import random
from uuid import uuid4


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Команда не распознана.")


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


boards = {}


def MakeKeyboard(board, idBoard, endGame):
    return [
        [
            InlineKeyboardButton(
                tiktaktoe.SYMBOLS[board[0]], callback_data=f'{idBoard},0' if not endGame else f'{idBoard},-1'),
            InlineKeyboardButton(
                tiktaktoe.SYMBOLS[board[1]], callback_data=f'{idBoard},1' if not endGame else f'{idBoard},-1'),
            InlineKeyboardButton(
                tiktaktoe.SYMBOLS[board[2]], callback_data=f'{idBoard},2' if not endGame else f'{idBoard},-1')
        ],
        [
            InlineKeyboardButton(
                tiktaktoe.SYMBOLS[board[3]], callback_data=f'{idBoard},3' if not endGame else f'{idBoard},-1'),
            InlineKeyboardButton(
                tiktaktoe.SYMBOLS[board[4]], callback_data=f'{idBoard},4' if not endGame else f'{idBoard},-1'),
            InlineKeyboardButton(
                tiktaktoe.SYMBOLS[board[5]], callback_data=f'{idBoard},5' if not endGame else f'{idBoard},-1')
        ],
        [
            InlineKeyboardButton(
                tiktaktoe.SYMBOLS[board[6]], callback_data=f'{idBoard},6' if not endGame else f'{idBoard},-1'),
            InlineKeyboardButton(
                tiktaktoe.SYMBOLS[board[7]], callback_data=f'{idBoard},7' if not endGame else f'{idBoard},-1'),
            InlineKeyboardButton(
                tiktaktoe.SYMBOLS[board[8]], callback_data=f'{idBoard},8' if not endGame else f'{idBoard},-1')
        ]
    ]


def start(update, context):
    global boards
    id = str(uuid4())
    board = tiktaktoe.NewBoard()
    boards[id] = board
    whoseMove = random.randint(0, 1)
    if whoseMove == tiktaktoe.X:
        update.message.reply_text('Вы ходите первым')
    else:
        update.message.reply_text('Я хожу первым')
        tiktaktoe.MoveAndCheck(board, tiktaktoe.BotMove(
            board, tiktaktoe.O), tiktaktoe.O)
    keyboard = MakeKeyboard(board, id, False)
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Ваш ход', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    global boards
    query = update.callback_query
    query.answer()
    id, move = query.data.split(',')
    move = int(move)
    if id in boards.keys():
        board = boards[id]
        gameStatus = tiktaktoe.MoveAndCheck(board, move, tiktaktoe.X)

        if gameStatus == tiktaktoe.NOT_END:
            botMove = tiktaktoe.BotMove(board, tiktaktoe.O)
            gameStatus = tiktaktoe.MoveAndCheck(board, botMove, tiktaktoe.O)

        if gameStatus in (tiktaktoe.X_WIN, tiktaktoe.O_WIN, tiktaktoe.DRAW):
            keyboard = MakeKeyboard(board, id, True)
            reply_markup = InlineKeyboardMarkup(keyboard)
            if gameStatus == tiktaktoe.X_WIN:
                query.edit_message_text(
                    'Вы победили', reply_markup=reply_markup)
            elif gameStatus == tiktaktoe.O_WIN:
                query.edit_message_text('Я победил', reply_markup=reply_markup)
            elif gameStatus == tiktaktoe.DRAW:
                query.edit_message_text('Ничья', reply_markup=reply_markup)
            boards.pop(id)
        elif gameStatus == tiktaktoe.NOT_END:
            keyboard = MakeKeyboard(board, id, False)
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_text('Ваш ход', reply_markup=reply_markup)


def help(update, context):
    msg = "/hello - Поздороваться\n/start - Запуск новой игры\n/exit - Выход\n/help - Это сообщение"
    update.message.reply_text(msg)
    exit()


def text(update, context):
    text_received = update.message.text
    update.message.reply_text(f'ECHO: "{text_received}"')


def error(update, context):
    pass
