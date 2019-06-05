# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters




def hello(bot, update):
    t = update.message.text
    if t == "qq":
        update.send("choose 1 or 2")
        if t == "1":
            update.send("1 choosen")
        if t == "2":
            update.message.reply_text("2 choosen")


def command(bot, update, args):
    update.message.reply_text("COOMAND")


updater = Updater('')

updater.dispatcher.add_handler(CommandHandler("zxc", command, pass_args=True))
text = MessageHandler(Filters.text, hello)
updater.dispatcher.add_handler(text)

updater.start_polling()
updater.idle()








