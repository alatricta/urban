import os
import asyncio
from telebot.async_telebot import AsyncTeleBot


api_key = os.getenv('TG_BOT')

bot = AsyncTeleBot(api_key)


@bot.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, text='Привет! Я бот помогающий твоему здоровью.')

@bot.message_handler(func=lambda message: True)
async def all_message(message):
    await bot.send_message(message.chat.id, text='Введите команду /start, чтобы начать общение.')

if __name__=='__main__':
    asyncio.run(bot.polling())
