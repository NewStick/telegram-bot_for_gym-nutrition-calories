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
from aiogram.client.session.aiohttp import AiohttpSession

# Импортируем некоторый список вспомогательных библиотек
# from os import getenv // на текущий момент TOKEN лежит в файле client_telegram_configuration.py вне виртуального пространства; однако в дальнейшем будет перенесено туда
# import sqlite3
from datetime import datetime
from client_telegram_configuration import TOKEN, PROXY_URL

client_dispatcher = Dispatcher()

@client_dispatcher.message(CommandStart())
async def command_start(user_message : Message):
    """ Создаём собственный обработчик для команды /start """
    print("[INFO] Collecting user data...")

    # Собираем некоторую информацию  о пользователе
    # user_id = str(user_message.from_user.id)
    # user_first_name = str(user_message.from_user.first_name)
    # user_last_name = str(user_message.from_user.last_name)

    # Данные для отправки сообщения пользователю в ответ
    reply_message_text = (
        "✅ <b>Вы активировали приложение</b> \n"
        "\nБлагодаря данному приложению вы сможете:"
        "\n• Возможность удобно и легко вести подсчёт дневного потребления Калорий, Белков, Жиров и Углеводов;"
        "\n• Наличие небольшого количества заранее подготовленных данных о продуктах питания;"
        "\n• Возможность задавать данные о собственных продуктах питания;"
        "\n• Получение статистики о питании за периоды: один день и один месяц."
    )
    await user_message.answer(reply_message_text)


@client_dispatcher.message(Command('help'))
async def command_help(user_message : Message):
    """ Создаём собственный обработчик для команды /help """
    pass

async def start_up_client_telegram():
    """ Основная функция, которая запускает бота """

    # Установим соединение Telegram бота через VPN тунель
    client_session = AiohttpSession(proxy=PROXY_URL)

    # Создаём переменную на основе класса Bot, который подключиться приложению Telegram
    client_telegram = Bot(
        token=TOKEN,
        session=client_session,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    # Совершаем постоянные запросы на сервер в проверках на новые зарегистрированные в Dispatcher события
    await client_dispatcher.start_polling(
        client_telegram,
        skip_updates = True
    )

if __name__ == "__main__":
    """ Точка входа в программу """
    try:
        program_start_time = datetime.now().time()
        print("[INFO] ProjectStart: запуск работы Telegram бота - {0.hour}-{0.minute}-{0.second}".format(program_start_time))
        asyncio.run(start_up_client_telegram())

    except KeyboardInterrupt:
        program_end_time = datetime.now().time()
        print("[INFO] ProjectEnd: завершение работы Telegram бота - {0.hour}-{0.minute}-{0.second}".format(program_end_time))
