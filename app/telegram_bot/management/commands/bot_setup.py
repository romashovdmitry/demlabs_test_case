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


async def main() -> None:
    """
    run Telegram bot
    """
    print('bot go')
    dp.include_routers(demlabs_router)
    await dp.start_polling(bot)

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        asyncio.run(main())