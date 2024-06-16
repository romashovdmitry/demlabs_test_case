# import connection to Redis
from main.utils import redis_con

# import constants
from order.constants import redis_basket_template

def get_redis_user_basket(func):
    def wrapper(*args, **kwargs):
        redis_user_basket_key = f"basket:user:{kwargs['redis_user_basket_key']}"

        if not redis_con.exists(redis_user_basket_key):
            redis_basket_user = redis_con.hset(
                redis_user_basket_key,
                mapping=redis_basket_template()
            )
            kwargs["redis_user_basket_key"] = redis_basket_user
            func(**kwargs)

        kwargs["redis_user_basket_key"] = redis_user_basket_key
        print(kwargs)
        func(**kwargs)

    return wrapper    


@get_redis_user_basket
def redis_add_to_basket(
    redis_user_basket_key: bytes,
    product_id: str,
    quantity: str
):
    """ add products to user basket """
#    redis_con.hset("basket:user:2", mapping={
#        'name': 'John',
#        "surname": 'Smith',
#        "company": 'Redis',
#        "age": 29
#    })
#    redis_con.hset(
#        redis_user_basket_key,
#        mapping={
#            'product_id': product_id,
#            "quantity": quantity,
#        })
    print("COME HERE 2 ")
    return