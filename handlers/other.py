import telebot

from init_bot import bot


@bot.message_handler(func=lambda _: True)
def unknown_com(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Не удалось определить команду !')
