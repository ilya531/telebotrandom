import random

import telebot

from funcs.datetime_funcs import get_welcome
from init_bot import bot


@bot.message_handler(commads=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = f'{get_welcome()}  Я бот-помощник по подбору пароля !)'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["start"])
def start_help(message: telebot.types.Message):
    text = f" {get_welcome()} Я бот-пароль.\n\n" \
           f"Cписок команд:\n" \
           f"/get_passw - Получить готовый пароль.\n" \
           f"/get_ip - Получить мой IP\n"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['get_passw'])
def get_passw(message: telebot.types.Message):
    with open('passw.txt', 'r', encoding='utf-8') as file:
        passw = file.read().split('/n')
    passw = random.choice(passw)
    bot.send_message(message.chat.id, text=f'Предлагаю такие варианты пароля:\n"{passw}"')


@bot.message_handler(commands=['get_ip'])
def get_ip(message: telebot.types.Message):
    text = f'Мой IP: {message.chat.location}'
    bot.send_message(message.chat.id, text)
