import telebot

from init_bot import bot


@bot.message_handler(func=lambda _: True)
def help_bit(message: telebot.types.Message):
    markup = telebot.util.quick_markup(
        {
            'Ссылка на интересный сайт': {'url': 'https://habr.com/ru/flows/popsci/articles/'},
            'Ссылка на рандомный ресурс': {'url': 'https://randomus.ru/?ysclid=ls0goeiux7620542383'}
        }
    )
    bot.reply_to(message, 'Может пригодится:', reply_markup=markup)


@bot.message_handler(func=lambda _: True)
def unknown_com(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Не удалось определить команду !')
