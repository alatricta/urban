from module_14_products_list import PRODUCTS
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

# main_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Купить', callback_data='purchase')],
#     [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
#     [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
#     ]
# )
main_menu_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Расчитать'), KeyboardButton(text='Информация')],
    [KeyboardButton(text='Купить')]
    ], resize_keyboard=True
)

males_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мужской', callback_data='male'),
     InlineKeyboardButton(text='Женский', callback_data='female')]
])

# product_kb = InlineKeyboardMarkup()
product_kb = []
for product in PRODUCTS:
    product_kb.append(
        [InlineKeyboardButton(text=product['name'],
                              callback_data='product_buying')])
product_kb = InlineKeyboardMarkup(inline_keyboard=product_kb)