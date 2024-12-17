from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio


api = '7300301439:AAF-jl92HiCspzGJ7eT6nvKQRDnGO13l2wI'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button1 = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Купить')
kb.row(button, button1, button2)

kb1 = InlineKeyboardMarkup(resize_keyboard=True)
button3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb1.row(button3, button4)

kb_buy = InlineKeyboardMarkup(resize_keyboard=True)
button_prod1 = InlineKeyboardButton(text='БАДы для мужчин', callback_data='product_buying')
button_prod2 = InlineKeyboardButton(text='БАДы для женщин', callback_data='product_buying')
button_prod3 = InlineKeyboardButton(text='БАДы для детей', callback_data='product_buying')
button_prod4 = InlineKeyboardButton(text='БАДы для беременных', callback_data='product_buying')
kb_buy.insert(button_prod1)
kb_buy.insert(button_prod2)
kb_buy.insert(button_prod3)
kb_buy.insert(button_prod4)

class UserState(StatesGroup):
    age = State()     # возраст
    growth = State()  # рост
    weight = State()  # вес

@dp.message_handler(commands=['start'])
async def start(message):
    #print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer(text='Выберите опцию:', reply_markup=kb1)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Для женщин: (10 x вес(кг)) + (6,25 x рост(см)) – (5 x возраст(г) – 161')
    await call.message.answer('Для мужчин: (10 x вес(кг)) + (6,25 x рост(см)) – (5 x возраст(г) + 5')

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open('files/1.jpg', 'rb') as img:
        await message.answer_photo(img, 'Название: GPL® Man | Описание: Комплекс пептидов GPL Man для мужчин | Цена: 15900 руб.')
    with open('files/2.jpg', 'rb') as img:
        await message.answer_photo(img, 'Название: Revilab ML 08 | Описание: Для женского организма 2+1 | Цена: 6600 руб.')
    with open('files/3.jpg', 'rb') as img:
        await message.answer_photo(img, 'Название: От A до Zn | Описание:  Витаминно-минеральный комплекс от А до Цинка для детей 3-7 лет груша | Цена: 209 руб.')
    with open('files/4.jpg', 'rb') as img:
        await message.answer_photo(img, 'Название: Фемибион | Описание:  Витаминно-минеральный комплекс для беременных | Цена: 28094 руб.')

    await message.answer('Выберите продукт для покупки:', reply_markup=kb_buy)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    woman = (10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161)
    man = (10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
    await message.answer(f'Норма калорий для женщин: {woman} ккал в сутки')
    await message.answer(f'Норма калорий для мужчин: {man} ккал в сутки')
    await UserState.weight.set()
    await state.finish()

@dp.message_handler()
async def all_massages(message):
    #print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)