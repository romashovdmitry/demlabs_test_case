""" small helper-functions that could be used in several or all apps """
# Python imports
import logging
from os import getenv
import inspect
import json
from PIL import Image

# Django imports
from django.core.exceptions import ValidationError

# import redis
import redis

# import constants
from order.constants import (
    REDIS_USER_BASKET_KEY_TEMPLATE,
    REPLACE_KEY
)

logger = logging.getLogger(__name__)


def define_image_file_path(
        filename: str,
        directory: str,
        object_type: str,
        instance_indicator: str
):
    """
    Define path for uploaded to API image.

    Parameters:
        filename: string with name of file
        directory: path where photoes are saved
            inside media directory
        instance: object of model Player, Club
            or another
    Returns:
        str: filename that would be used for
            saving file in project
            
    """
    try:
        return directory + instance_indicator + object_type + filename.split(".")[-1]

    except Exception as ex:
        logger.error(
            f'main.utils.define_image_file_path: {ex}'
        )

        return filename


def create_redis_conn():
 
    if int(getenv("IS_PROD")):
        redis_con = redis.Redis(
            host=getenv("REDIS_HOST", default="127.0.0.1"),
            port=int(getenv("REDIS_PORT", default=6379)),
            db=int(getenv("REDIS_DATABASE", default=0)),
        )

        return redis_con
    
    else:
        redis_con = redis.Redis(
            host="127.0.0.1",
            port=6379,
            db=0,
        )

        return redis_con    


redis_con = create_redis_conn()


# FIXME: дописать аннотирование, см. внимательно
def define_image_file_path(
        filename: str,
        directory: str,
        object_type: str,
        instance_indicator: str
):
    """
    Define path for uploaded to API image.

    Parameters:
        filename: string with name of file
        directory: path where photoes are saved
            inside media directory
        instance: object of model Player, Club
            or another
    Returns:
        str: filename that would be used for
            saving file in project
            
    """
    try:
        return directory + instance_indicator + object_type + filename.split(".")[-1]

    except Exception as ex:
        # FIXME: здесь логгирование должно быть
        logger.error(
            f'main.utils.define_image_file_path: {ex}'
        )

        return filename


# NOTE: добавить аннотирование типа данных
# расширить (Parameters, Returns) аннотацию ф-ции
def image_file_extension_validator(object):
    """
    Check file-extension for case when format
    in filename not equal to real format. 
    For example, example.jpc could be filename,
    but jpg is real file-extension.
    """
    try:

        image_format = Image.open(object).format
        filename = str(object)
        filename_file_extension = filename.split(".")[-1]

        if not (image_format.lower() in ["jpeg", "jpg"] and filename_file_extension.lower() in ["jpeg", "jpg"]):

            if image_format.lower() != filename_file_extension.lower():

                raise ValidationError(
                    "Real file-extension is not equal to "
                    "file-extension in filename. "
                    "Please, redefine filename by the correct way. "
                    f"Filename: {str(object)}"
                )

        return object

    except Exception as ex:
        # FIXME: здесь логгирование должно быть
        print(ex)
        raise ValidationError(
            "Real file-extension is not equal to "
            "file-extension in filename. "
            "Please, redefine filename by the correct way."
            f"Filename: {str(object)}"
        )
    
# https://stackoverflow.com/a/24628710
foo_name = lambda: inspect.stack()[1][3]


logger = logging.getLogger(__name__)

redis_decode_hash = lambda d: {key.decode('utf-8'): value.decode('utf-8') for key, value in d.items()}
redis_decode_list = lambda list_: [json.loads(elem) for elem in list_]
get_user_id_from_redis_basket_key = lambda str_: int(
    str_.replace(
        REDIS_USER_BASKET_KEY_TEMPLATE.replace(
            REPLACE_KEY,
            ""
        ), ""
    )
)
redis_basket_sum = lambda list_: sum(element["purchase_price"] * element["quantity"] for element in list_)
define_redis_basket_key = lambda int_: REDIS_USER_BASKET_KEY_TEMPLATE.replace(REPLACE_KEY, str(int_))