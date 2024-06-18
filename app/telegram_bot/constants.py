# import constants
from main.constants import REPLACE_KEY

# NAME = {text: callback_data}
TELEGRAM_BUTTON_CALLBACK = f"order_number:{REPLACE_KEY}"
TELEGRAM_BUTTON = {
    "Заказ отправлен!": TELEGRAM_BUTTON_CALLBACK
}

NEW_ORDER_NOTIFY_TEXT = f"Новый заказ под номером: {REPLACE_KEY}"

SUCCESS_UPDATE_STATUS = "Статус успешно обновился!"
UNSUCESS_UPDATE_STATUS = "Статус не обновился!"