from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

import asyncio
import logging

from config import *
from keyboards import *
import texts

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

import asyncio
import logging

from config import *
from keyboards import *
# from admin import *
# from db import *
from crud_functions import *
import texts

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Добро пожаловать, {message.from_user.username}! {texts.start}', reply_markup = start_kb)

@dp.message_handler(text='О нас')
async def price(message):
    await message.answer(texts.about, reply_markup = start_kb)

@dp.message_handler(text='Стоимость')
async def info(message):
    await message.answer('Что вас интересует?', reply_markup = catalog_kb)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    all_products = get_all_products()
    with open("images/Pizza.png", 'rb') as img:
        await message.answer_photo(img, f'Название: {all_products[0][0]} | Описание: {all_products[0][1]} | Цена: {all_products[0][2]}')
    with open("images/Sushi.png", 'rb') as img:
        await message.answer_photo(img, f'Название: {all_products[1][0]} | Описание: {all_products[1][1]} | Цена: {all_products[1][2]}')
    with open("images/Burger.png", 'rb') as img:
        await message.answer_photo(img, f'Название: {all_products[2][0]} | Описание: {all_products[2][1]} | Цена: {all_products[2][2]}')
    with open("images/Shaurma.png", 'rb') as img:
        await message.answer_photo(img, f'Название: {all_products[3][0]} | Описание: {all_products[3][1]} | Цена: {all_products[3][2]}')
    await message.answer('Выберите товар для покупки:', reply_markup = catalog_food_kb)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.callback_query_handler(text="small")
async def buy_s(call):
    await call.message.answer(texts.Sgame, reply_markup = buy_kb)
    await call.answer()

@dp.callback_query_handler(text="medium")
async def buy_m(call):
    await call.message.answer(texts.Mgame, reply_markup = buy_kb)
    await call.answer()

@dp.callback_query_handler(text="big")
async def buy_l(call):
    await call.message.answer(texts.Lgame, reply_markup = buy_kb)
    await call.answer()

@dp.callback_query_handler(text="other")
async def buy_other(call):
    await call.message.answer(texts.other, reply_markup = buy_kb)
    await call.answer()


@dp.callback_query_handler(text='back_to_catalog')
async def back(call):
    await call.message.answer('Что вас интересует?', reply_markup = catalog_kb)
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)