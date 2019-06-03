# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler




def hello(bot, update, args):
    update.message.reply_text("HIIII")


updater = Updater('714097148:AAHsIAhDvwU5NzdBM1KOJbJCIwXTx7qU918')

updater.dispatcher.add_handler(CommandHandler("question", hello, pass_args=True))

updater.start_polling()
updater.idle()
