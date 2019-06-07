# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters


class DialogBot(object):
    FIRST, SECOND = range(2)


    def __init__(self, token):

        conv_handler = ConversationHandler(
            entry_points=[MessageHandler(Filters.text, self.start)],
            states={
                DialogBot.FIRST: [CallbackQueryHandler(self.first)]
            },
            fallbacks=[MessageHandler(Filters.text, self.start)]
        )
        self.updater = Updater(token=token)  # заводим апдейтера
        self.updater.dispatcher.add_handler(conv_handler)  # ставим обработчик всех текстовых сообщений



    def begin(self):
        self.updater.start_polling()

        self.updater.idle()



    test = [{"question": "Найбільш інформативним методом діагностики діафрагмальної кили є11111:",
             'first_letters': 'німд',
             "answers": [
                 {"percent": "0%",
                  "text": "Езофаготонокімографія"},
                 {"percent": "0%",
                  "text": "Езофагоскопія"},
                 {"percent": "0%",
                  "text": "Ультразвукове дослідження"},
                 {"percent": "0%",
                  "text": "Комп'ютерна томографія"},
                 {"percent": "100%",
                  "text": "Рентгенограма шлунка в горизонтальному та вертикальному положенні хворого із застосуванням барію"},
             ]},
            {"question": "Найбільш інформативним методом діагностики діафрагмальної кили є22222:",
             'first_letters': 'німд',
             "answers": [
                 {"percent": "0%",
                  "text": "Езофаготонокімографія"},
                 {"percent": "0%",
                  "text": "Езофагоскопія"},
                 {"percent": "0%",
                  "text": "Ультразвукове дослідження"},
                 {"percent": "0%",
                  "text": "Комп'ютерна томографія"},
                 {"percent": "100%",
                  "text": "Рентгенограма шлунка в горизонтальному та вертикальному положенні хворого із застосуванням барію"},
             ]}
            ]

    def start(self, bot, update):
        print(update.message.text.lower())
        print(update.message.text == "німд")
        count = 0
        result = []
        for i in DialogBot.test:
            if update.message.text.lower() == i["first_letters"]:
                result.append(i)
                count += 1
        if count == 1:
            answers = "".join("%s - %s \n" % (i['percent'], i['text']) for i in DialogBot.test[0]['answers'])
            answer = f"{result[0]['question']}\n{answers} "
            update.message.reply_text(answer)
        if count > 1:
            keyboard = []
            for i in result:
                button = [InlineKeyboardButton(i['question'], callback_data=str(DialogBot.FIRST))]
                keyboard.append(button)
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text(
                u"Выбери вопрос",
                reply_markup=reply_markup
            )
        return DialogBot.FIRST

    def first(self, bot, update):
        query = update.callback_query
        print(query.message)

        keyboard = [
            [InlineKeyboardButton(u"Next", callback_data=str(DialogBot.SECOND))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=u"First CallbackQueryHandler, Press next111111"
        )

        reply_markup = InlineKeyboardMarkup(keyboard)

        bot.edit_message_reply_markup(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            reply_markup=reply_markup
        )
        return DialogBot.SECOND



if __name__ == "__main__":
    token = "714097148:AAHsIAhDvwU5NzdBM1KOJbJCIwXTx7qU918"
    dialog_bot = DialogBot(token)
    dialog_bot.begin()
