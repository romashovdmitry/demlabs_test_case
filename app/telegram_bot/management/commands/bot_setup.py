# Python imports
import asyncio

# Django imports
from django.core.management.base import BaseCommand

# Telegram imports
from aiogram import Dispatcher

# import constants, config data
from main.settings import bot

# import custom foos, classes
from telegram_bot.handlers import demlabs_router

dp = Dispatcher()


#  https://docs.aiogram.dev/en/stable/#simple-usage
async def main() -> None:
    """
    Ф-ция запускает работу бота.
    """
    print('bot go')
    dp.include_routers(demlabs_router)
    await dp.start_polling(bot)


class Command(BaseCommand):
    """
    Запускает бот-пуллинг телеграмм-бота
    """

    def handle(self, *args, **options):

        asyncio.run(main())
