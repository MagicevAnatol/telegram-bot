from telebot.handler_backends import State, StatesGroup


class UserInputInfo(StatesGroup):
    input_city = State()  # данные введённые пользователем
    user_select_id = State()  # выбранный вариант пользователем
    date_of_entry = State()  # дата заезда
    date_of_departure = State()  # дата выезда
