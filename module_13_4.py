from aiogram import Bot, Dispatcher,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

import asyncio


api = '7300301439:AAF-jl92HiCspzGJ7eT6nvKQRDnGO13l2wI'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()     # возраст
    growth = State()  # рост
    weight = State()  # вес

@dp.message_handler(commands=['start'])
async def start(message):
    #print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью. Напишите "Калории" и я рассчитаю суточную норму калорий.')

@dp.message_handler(text=['Colories', 'Калории', 'Ккал', 'К', 'к'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
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
