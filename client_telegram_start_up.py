"""
ℹ️ Основной файл проекта, откуда запускается данный Telegram бот

Здесь описываются следующие настройки:
- Импорт всех библиотек для запуска бота;
- Создание объектов класса Router, т.е. подключаение каждого из модулей;
- Создание команды /start и /help с последующей верификацией пользователя.
"""

# Импортируем все необходимые части из Aiogram
import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# Импортируем некоторый список вспомогательных библиотек
# from os import getenv // на текущий момент TOKEN лежит в файле client_telegram_configuration.py вне виртуального пространства; однако в дальнейшем будет перенесено туда
from datetime import datetime
from client_telegram_configuration import TOKEN

client_dispatcher = Dispatcher()

@client_dispatcher.message(CommandStart())
async def command_start(user_message : Message):
    """ Создаём собственный обработчик для команды /start """
    pass

@client_dispatcher.message(Command('help'))
async def command_help(user_message : Message):
    """ Создаём собственный обработчик для команды /help """
    pass

async def start_up_client_telegram():
    """ Основная функция, которая запускает бота """

    # Создаём переменную на основе класса Bot, который подключиться приложению Telegram
    client_telegram = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Совершаем постоянные запросы на сервер в проверках на новые зарегистрированные в Dispatcher события
    await client_dispatcher.start_polling(client_telegram)

if __name__ == "__main__":
    """ Точка входа в программу """
    try:
        program_start_time = datetime.now().time()
        print("[INFO] Запускаем Telegram бота - {0.hour}-{0.minute}-{0.second}".format(program_start_time))
        asyncio.run(start_up_client_telegram())

    except KeyboardInterrupt:
        program_end_time = datetime.now().time()
        print("[INFO] Работа Telegram бота завершена - {0.hour}-{0.minute}-{0.second}".format(program_end_time))
