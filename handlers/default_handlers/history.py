from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["history"])
def bot_start(message: Message):
    bot.reply_to(message, f"Тут будет ваша история поиска!")
