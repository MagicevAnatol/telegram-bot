from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["highprice"])
def bot_start(message: Message):
    bot.reply_to(message, f"Тут будет сортировка по убыванию.")
