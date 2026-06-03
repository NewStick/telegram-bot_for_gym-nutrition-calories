from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

food_settings = Router()

async def create_food_settings_keyboard():
    """ Функция возвращает объект ReplyKeyboard настроенный для Module_FoodSettings """
    pass