from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!\n"
                          f"Я бот для поиска лучших предложений по отелям по всему миру!\n"
                          f"Что бы начать работу, выбери действие.\n"
                          f"Введите команду /help что бы увидеть все команды бота.")
