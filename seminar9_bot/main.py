from mytoken import TOKEN
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, CallbackQueryHandler
from command import *


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text))
updater.dispatcher.add_error_handler(error)

print("Бот запущен.")
updater.start_polling()
updater.idle()
