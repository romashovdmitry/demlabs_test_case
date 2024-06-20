"""
handler callbacks: taps of the button
"""
# Python imports
import asyncio

# Telegram imports
from typing import Any
from aiogram import Router
from aiogram.handlers import CallbackQueryHandler

# import models
from order.models.orders import Order

# import constants
from telegram_bot.constants import (
    NEW_ORDER_NOTIFY_TEXT,
    REPLACE_KEY,
    SUCCESS_UPDATE_STATUS,
    UNSUCESS_UPDATE_STATUS,
    TELEGRAM_BUTTON_CALLBACK
)
from order.constants import OrderStatus

# import custom foos, classes
from telegram_bot.services import telegram_log_errors
from main.utils import foo_name

demlabs_router = Router()

@demlabs_router.callback_query()
class AdminQueryHandler(CallbackQueryHandler):
    '''
    For processing taps on button in Telegram group
    '''
    async def handle(self) -> Any:
        try:

            order_numbber = int(
                self.callback_data.replace(
                    TELEGRAM_BUTTON_CALLBACK.replace(REPLACE_KEY, ""),
                    ""
                )
            )

            order = await Order.objects.aget(pk=order_numbber)
            order.delivery_status = OrderStatus.DELIVERED
            await order.asave()

            self.message.reply_markup.inline_keyboard[0][0] = None
            await self.message.edit_reply_markup(reply_markup=self.message.reply_markup)

            await self.message.answer(
                text=SUCCESS_UPDATE_STATUS
            )

        except Exception as ex:
            await telegram_log_errors(
                f'[{foo_name()}]'
                f'Ex text: {str(ex)}'
            )
            await self.message.answer(
                text=UNSUCESS_UPDATE_STATUS
            )