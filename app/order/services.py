# python imports
from os import getenv
from datetime import timedelta
import json
import asyncio

# import connection to Redis
from main.utils import redis_con

# import models
from user.models.user import User
from order.models.orders import Order
from order.models.order_items import OrderItems
from product.models.product import Product

# import constants
from main.constants import BASKET_TIME
from order.constants import (
    redis_basket_template,
    REPLACE_KEY,
    REDIS_PRODUCT_BASKET_NOUNT_TEMPLATE
)

# import custom foos, classes
from main.utils import (
    redis_decode_list,
    get_user_id_from_redis_basket_key,
    redis_basket_sum,
    define_redis_basket_key,
    foo_name,
    define_user_basket_key
)
from telegram_bot.services import telegram_log_errors


def get_redis_user_basket(func):
    """
    Decorator create new key value for user
    if not exists. And set expire time for every
    new action with users's basket.
    """
    def wrapper(*args, **kwargs):
        kwargs["user_id"] = kwargs['redis_user_basket_key']
        kwargs['redis_user_basket_key'] = define_redis_basket_key(
            kwargs['redis_user_basket_key'])

        func(**kwargs)

        redis_con.expire(
            kwargs['redis_user_basket_key'], BASKET_TIME)

    return wrapper


@get_redis_user_basket
def redis_add_to_basket(
    **kwargs,
):
    """
    Saving new product in basket.

    Parameters:
        redis_user_basket_key: Redis key for request user
        **kwargs: Additional keyword arguments may include:
            - product_id (int): The ID of the product being added.
            - quantity (int): The quantity of the product being added.
            - price (int): The price of the product being added in moment.
            - product_object (Product): Product model object of the product
                being added.
            - user_id (int): request user pk in out database
    """
    try:

        kwargs["product_object"].setup_redis_reserved_mount_by_user(
            items_quantity=kwargs.get("quantity"),
            user_id=kwargs.get("user_id"),
            previous_quantity=kwargs.get(
                "previous_basket_product", {}).get("quantity", 0
            )
        )

        del kwargs["product_object"]
        del kwargs["user_id"]

        with redis_con.pipeline() as pipe:
            pipe.multi()

            if kwargs["previous_basket_product"]:
                pipe.lrem(
                    kwargs["redis_user_basket_key"],
                    0,
                    json.dumps(kwargs["previous_basket_product"])
                )

            del kwargs["previous_basket_product"]

            pipe.lpush(
                kwargs["redis_user_basket_key"],
                json.dumps(kwargs)
            )
            pipe.execute()

        return

    except Exception as ex:
        asyncio.run(
            telegram_log_errors(
                f'[{foo_name()}]'
                f'Ex text: {str(ex)}'
            )
        )


def create_order_from_basket(
        user: User
):
    """
    1. Get order items reserved by basket.
    """
    redis_user_basket_key = define_user_basket_key(user.pk)

    basket_items = redis_decode_list(
        redis_con.lrange(
                redis_user_basket_key, 0, -1
            )
        )

    redis_con.delete(redis_user_basket_key)

    OrderItems().create_order_items(
        user=user,
        order=Order().create_new_order(
            user=user,
            sum=redis_basket_sum(basket_items)
        ),
        basket_items=basket_items
    )

    return


def get_basket_items(user: User):
    """get bakset """
    redis_user_basket_key = define_user_basket_key(user.pk)
    basket_items = redis_decode_list(
        redis_con.lrange(
                redis_user_basket_key, 0, -1
            )
        )

    return_list__dict = []

    for basket in basket_items:
        return_list__dict.append(
            {
                "name": Product.objects.get(pk=basket["product"]).name,
                "category": Product.objects.get(pk=basket["product"]).category,
                "quantity": basket["quantity"],
                "purchase_price": basket["purchase_price"],
                "product_image": Product.objects.get(pk=basket["product"]).product_image.url
            }
        )

    return return_list__dict


def delete_redis_product(
        user_pk: User.pk, product_pk: int
):
    redis_user_basket_key = define_user_basket_key(user.pk)
    with redis_con.pipeline() as pipe:
        pipe.multi()
        redis_con.hdel(
            REDIS_PRODUCT_BASKET_NOUNT_TEMPLATE.replace(
                REPLACE_KEY, str(product_pk)
            ),
            user_pk
        )
        redis_con.hdel(
            redis_user_basket_key, user_pk 
        )
        pipe.execute()

    return
