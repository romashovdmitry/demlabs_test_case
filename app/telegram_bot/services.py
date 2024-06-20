# Python imports
from os import getenv
import logging

# Telegram imports
from aiogram.utils.keyboard import InlineKeyboardBuilder

# import models
from order.models.orders import Order  # for typing

# import config data, constants
from main.settings import bot
from main.utils import logger
from telegram_bot.constants import TELEGRAM_BUTTON, NEW_ORDER_NOTIFY_TEXT, REPLACE_KEY


async def telegram_log_errors(exception_text: str) -> None:
    """
    To log errors 
    
    exception_text (str): text of exception
    """
    try:
        await bot.send_message(
            chat_id=getenv("DEVELOPER_TELEGRAM_ID", 442442997),
            text=exception_text
        )

    except Exception as ex:
        # FIXME: заменить/добавить логгирование в файл, logging
        logger.error(f"[telegram_log_errors] {ex}")

    logger.error(exception_text)


async def send_new_order_message(order_number: Order.pk) -> None:
    """
    Send notify message about new order to Telegram group

    Parameters:
        order_number (Order.pk): Order's object primare key
            of created order.
    """
    # -4224556894 - group for test on local
    DEVELOPER_TELEGRAM_ID = getenv("DEVELOPER_TELEGRAM_ID", 442442997) 
    telegram_button_builder = InlineKeyboardBuilder()

    for text, callback_data in TELEGRAM_BUTTON.items():
        telegram_button_builder.button(
            text=text,
            callback_data=callback_data.replace(
                REPLACE_KEY, str(order_number)
            )
        )
    telegram_button_builder.adjust(1)

    await bot.send_message(
        chat_id=DEVELOPER_TELEGRAM_ID,
        text=NEW_ORDER_NOTIFY_TEXT.replace(REPLACE_KEY, str(order_number)),
        reply_markup=telegram_button_builder.as_markup()
    )
