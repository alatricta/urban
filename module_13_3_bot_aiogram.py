import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.state import State, StatesGroup 
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    Message, 
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    ReplyKeyboardRemove
)

api_key = os.getenv('TG_BOT')

bot = Bot(api_key)
dp = Dispatcher(storage=MemoryStorage())


class UserState(StatesGroup):
    male = State()
    age = State()
    growth = State()
    weight = State()


@dp.message(F.text.casefold().in_(['calories', 'калории']))
@dp.message(CommandStart())
async def set_male(message: Message, state: FSMContext):
    await state.set_state(UserState.male)
    
    males = ['Мужской', 'Женский']
    buttons = [KeyboardButton(text=m) for m in males]
    keyboard = ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True)

    await message.answer(text='Укажите свой пол:', reply_markup=keyboard)
    

# @dp.message(UserState.male, func=lambda message: message.text.isdigit())
@dp.message(UserState.male, F.text.casefold().in_(['мужской', 'женский']))
async def set_age(message: Message, state: FSMContext):
    await state.update_data(male=message.text)
    await state.set_state(UserState.age)
    await message.answer(text='Введите свой возраст:', reply_markup=ReplyKeyboardRemove())


@dp.message(UserState.age, F.text.isdigit().is_(True))
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(UserState.growth)
    await message.answer(text='Введите свой рост:')


@dp.message(UserState.growth, F.text.isdigit().is_(True))
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await state.set_state(UserState.weight)
    await message.answer('Введите свой вес:')


@dp.message(UserState.weight, F.text.isdigit())
async def send_calories(message: Message, state: FSMContext):
    data = await state.update_data(weight=message.text)
    # data = await state.get_data()
    await state.clear()

    male = data['male']
    weight = data['weight']
    growth = data['growth']
    age = data['age']

    if male.casefold() == 'мужской':
        calories = 10*int(weight) + 6.25*int(growth) - 5*int(age) + 5
    else:
        calories = 10*int(weight) + 6.25*int(growth) - 5*int(age) - 161

    await message.answer(f'{calories}')


@dp.message(Command('cancel'))
@dp.message(F.text.casefold().in_(['cancel', 'отмена']))
async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer(text="Cancelled", reply_markup=ReplyKeyboardRemove())


# Почему то не работает. Так и не понял почему =(
# @dp.message()
# async def all_message(message: Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is not None:
#         message.reply(text='Я вас не понимаю')
#     else:
#         message.reply('Для начала напишите команду: "Calories", для отмены "Canseled"')


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
