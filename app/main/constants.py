# Python imports
from os import getenv
from datetime import timedelta

REPLACE_KEY = "<KEY>"


BASKET_TIME = timedelta(minutes=getenv("REDIS_BASKET_TIME", 30))