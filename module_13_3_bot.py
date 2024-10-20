import os
import asyncio
from telebot import asyncio_filters
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_storage import StateMemoryStorage
from telebot.states import State, StatesGroup
from telebot.states.asyncio.context import StateContext
from telebot.states.asyncio.middleware import StateMiddleware
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, Message



api_key = os.getenv('TG_BOT')
state_storage = StateMemoryStorage()
bot = AsyncTeleBot(api_key, state_storage=state_storage)

bot.add_custom_filter(asyncio_filters.IsDigitFilter())
bot.add_custom_filter(asyncio_filters.StateFilter(bot))
bot.add_custom_filter(asyncio_filters.TextMatchFilter())

bot.setup_middleware(StateMiddleware(bot))


class UserState(StatesGroup):
    male = State()
    age = State()
    growth = State()
    weight = State()


@bot.message_handler(text=['Calories'])
async def set_male(message, state: StateContext):
    await state.set(UserState.male)
    
    keyboard = ReplyKeyboardMarkup()
    males = ['Мужской', 'Женский']
    buttons = [KeyboardButton(m) for m in males]
    keyboard.add(*buttons)

    await bot.reply_to(message, text='Укажите свой пол:', reply_markup=keyboard)


@bot.message_handler(state=UserState.male, text=['Мужской', 'Женский'])
async def set_age(message, state: StateContext):
    await state.set(UserState.age)
    await bot.reply_to(message, text='Введите свой возраст:')
    await state.add_data(male=message.text)


@bot.message_handler(state="*", commands=["cancel"])
async def clear_state(message, state: StateContext):
    await state.delete()
    await bot.send_message(message.chat.id, 'Операция прервана. Чтобы начать сначала напишите: "Calories"')


@bot.message_handler(state=UserState.age, is_digit=True)
async def set_growth(message, state: StateContext):
    await state.set(UserState.growth)
    await bot.reply_to(message, text='Введите свой рост:')
    await state.add_data(age = message.text)


@bot.message_handler(state=UserState.growth, is_digit=True)
async def set_weight(message, state):
    await state.set(UserState.weight)
    await bot.reply_to(message,'Введите свой вес:')
    await state.add_data(growth = message.text)


@bot.message_handler(state=UserState.weight, is_digit=True)
async def send_calories(message, state):
    async with state.data() as data:
        male = data.get('male')
        age = data.get('age')
        growth = data.get('growth')
        weight = message.text

    if male == 'Мужской':
        calories = 10*int(weight) + 6.25*int(growth) - 5*int(age) + 5
    else:
        calories = 10*int(weight) + 6.25*int(growth) - 5*int(age) - 161

    await bot.reply_to(message,f'{calories}')

    await state.delete()


if __name__=='__main__':
    asyncio.run(bot.polling())
