from mytoken import TOKEN
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, CallbackQueryHandler
from command import *


updater = Updater(TOKEN)


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        SELECT: [CommandHandler('viewall', ViewAll),
                 CommandHandler('add', AddItem),
                 CommandHandler('filter', ViewFilter),
                 CommandHandler('remove', RemoveItem),
                 CommandHandler('departments', ViewDepartments),
                 CommandHandler('positions', ViewPositions),
                 CommandHandler('save', SaveDB)
                 ],

        # Add State
        INPUTNAME: [MessageHandler(Filters.text & ~Filters.command, InputName),
                    CommandHandler('cancel', CancelAdd)],
        INPUTTEL: [MessageHandler(Filters.text & ~Filters.command, InputTel),
                   CommandHandler('cancel', CancelAdd)],
        INPUTDEP: [MessageHandler(Filters.text & ~Filters.command, InputDepartment),
                   CommandHandler('cancel', CancelAdd)],
        INPUTPOS: [MessageHandler(Filters.text & ~Filters.command, InputPosition),
                   CommandHandler('cancel', CancelAdd)],

        # Filter State
        INPUTFILTER: [MessageHandler(Filters.text & ~Filters.command, InputFilter),
                      CommandHandler('cancel', CancelFilter)],

        # Remove State
        INPUTID: [MessageHandler(Filters.text & ~Filters.command, InputID),
                  CommandHandler('cancel', CancelRemove)],
        CONFIRMREM: [CommandHandler('confirm', ConfirmRemove),
                     CommandHandler('cancel', CancelRemove)]
    },
    fallbacks=[CommandHandler('done', Done)],
)

updater.dispatcher.add_handler(conv_handler)
updater.dispatcher.add_handler(MessageHandler(Filters.command, Unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, Text))

print("Бот запущен.")
updater.start_polling()
updater.idle()
