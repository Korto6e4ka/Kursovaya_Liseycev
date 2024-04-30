from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from parse import squares_list, museums_list, parks_list, monuments_list, places_list
import random

def main_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text=f'💥 Площади и скверы', callback_data='check_squares')
    kb.button(text=f'⭐️ Музеи и культурные объекты', callback_data='check_museums')
    kb.button(text=f'🦜 Парки и зоны отдыха', callback_data='check_parks')
    kb.button(text=f'🪙 Архитектурные памятники и сооружения', callback_data='check_monuments')
    kb.button(text=f'🪧 Интересные места', callback_data='check_places')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


start_router = Router()

emotions = ['😌 Вам обязательно понравится', '😌 Вы останетесь в восторге', '😍 и возьмте с собой вторую половинку', '😍 эмоции на весь день обеспечены', '💥 впечатления на весь день гарантированы']

@start_router.message(Command(commands='start'))
async def hello_windows(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,'Здравствуйте 🙌 \n\n 🤖 расскажу Вам куда сходить в Тюмене', reply_markup=main_kb())


@start_router.callback_query(F.data.startswith('check_squares'))
async def echo_message(call: CallbackQuery):
    item = squares_list
    value = random.choice(item)
    emotion = random.choice(emotions)
    await call.message.answer(f'Посетите: {value}\n\n'
                              f'{emotion}')
    await call.answer()


@start_router.callback_query(F.data.startswith('check_museums'))
async def echo_museums(call: CallbackQuery):
    item = museums_list
    value = random.choice(item)
    emotion = random.choice(emotions)
    await call.message.answer(f'Посетите: {value}\n\n'
                              f'{emotion}')
    await call.answer()

@start_router.callback_query(F.data.startswith('check_parks'))
async def echo_parks(call: CallbackQuery):
    item = museums_list
    value = random.choice(item)
    emotion = random.choice(emotions)
    await call.message.answer(f'Посетите: {value}\n\n'
                              f'{emotion}')
    await call.answer()


@start_router.callback_query(F.data.startswith('check_monuments'))
async def echo_monuments(call: CallbackQuery):
    item = monuments_list
    value = random.choice(item)
    emotion = random.choice(emotions)
    await call.message.answer(f'Посетите: {value}\n\n'
                              f'{emotion}')
    await call.answer()


@start_router.callback_query(F.data.startswith('check_places'))
async def echo_monuments(call: CallbackQuery):
    item = places_list
    value = random.choice(item)
    emotion = random.choice(emotions)
    await call.message.answer(f'Посетите: {value}\n\n'
                              f'{emotion}')
    await call.answer()