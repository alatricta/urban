import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)

api_key = os.getenv('TG_BOT')

bot = Bot(api_key)
dp = Dispatcher(storage=MemoryStorage())


class UserState(StatesGroup):
    male = State()
    age = State()
    growth = State()
    weight = State()


@dp.message(CommandStart())
@dp.message(F.text.casefold() == 'расчитать')
async def main_menu(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
        ]
    )

    await message.reply('Выберите опцию:', reply_markup=kb)


@dp.callback_query(F.data == 'formulas')
async def get_formulas(call: CallbackQuery):
    await call.answer()

    formulas = 'Формулы для расчёта:\n'\
        'Для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n'\
        'Для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161'

    await call.message.answer(formulas)


@dp.callback_query(F.data == 'calories')
async def set_male(call: CallbackQuery, state: FSMContext):
    await call.answer()

    await state.set_state(UserState.male)

    males = ['Мужской', 'Женский']
    calls = ['male', 'female']
    buttons = [InlineKeyboardButton(text=m, callback_data=c) for m,c in zip(males, calls)]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons])

    await call.message.answer(text='Укажите свой пол:', reply_markup=keyboard)


@dp.callback_query(UserState.male, F.data.in_(['male', 'female']))
async def set_age(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.update_data(male=call.data)
    await state.set_state(UserState.age)
    await call.message.answer(text='Введите свой возраст:')


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
    await state.clear()

    male = data['male']
    weight = data['weight']
    growth = data['growth']
    age = data['age']

    if male.casefold() == 'male':
        calories = 10*int(weight) + 6.25*int(growth) - 5*int(age) + 5
    else:
        calories = 10*int(weight) + 6.25*int(growth) - 5*int(age) - 161

    await message.answer(f'Ваша норама калорий: {calories}')


@dp.message(Command('cancel'))
@dp.message(F.text.casefold().in_(['cancel', 'отмена']))
async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer(text="Cancelled", reply_markup=ReplyKeyboardRemove())


@dp.message()
async def all_message(message: Message, state: FSMContext):

    current_state = await state.get_state()

    if current_state is not None:
        await message.reply(text='Я вас не понимаю')
    else:
        await message.answer(
            'Для начала напишите команду: "/start" или слово "расчитать", для отмены наберите "сancel"'
        )


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
