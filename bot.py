# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters

TELEGRAM_HTTP_API_TOKEN = ''

FIRST, SECOND = range(2)

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


def start(bot, update):
    print(update.message.text.lower())
    print(update.message.text == "німд")
    count = 0
    result = []
    for i in test:
        if update.message.text.lower() == i["first_letters"]:
            result.append(i)
            count += 1
    if count == 1:
        answers = "".join("%s - %s \n" % (i['percent'], i['text']) for i in test[0]['answers'])
        answer = f"{result[0]['question']}\n{answers} "
        update.message.reply_text(answer)
    if count > 1:
        keyboard = []
        for i in result:
            button = [InlineKeyboardButton(i['question'], callback_data=str(FIRST))]
            keyboard.append(button)
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(
            u"Выбери вопрос",
            reply_markup=reply_markup
        )
    return FIRST

def first(bot, update):
    query = update.callback_query
    print(query.message)

    keyboard = [
        [InlineKeyboardButton(u"Next", callback_data=str(SECOND))]
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
    return SECOND


updater = Updater(TELEGRAM_HTTP_API_TOKEN)

conv_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.text, start)],
    states={
        FIRST: [CallbackQueryHandler(first)]
    },
    fallbacks=[MessageHandler(Filters.text, start)]
)

updater.dispatcher.add_handler(conv_handler)

updater.start_polling()

updater.idle()




