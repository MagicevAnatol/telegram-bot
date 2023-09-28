from telebot.types import Message
from states.user_data import UserInputInfo
from loader import bot
from utils.find_distantion_id import destination_id


@bot.message_handler(commands=["lowprice"])
def low_price(message: Message):
    bot.set_state(message.from_user.id, UserInputInfo.input_city, message.chat.id)
    bot.send_message(message.from_user.id, f"Ищем отели по возврастанию цены, введите город: ")


@bot.message_handler(state=UserInputInfo.input_city)
def find_city(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["input_city"] = message.text

    bot.send_message(message.from_user.id, f"Выполняю поиск в городе: {data['input_city']}")
    possible_options = destination_id(data["input_city"])

    print(possible_options)
