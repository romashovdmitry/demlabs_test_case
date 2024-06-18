# Django imports
from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models.orders import Order

# import custom foos, classes
from telegram_bot.services import send_new_order_message

@receiver(post_save, sender=Order)
async def order_created_signal(sender, instance, created, **kwargs):
    """
    This signal handler is triggered after a new Order instance is saved.

    Parameters:
        sender (Order): The Order model class.
        instance (Order): The newly created Order instance.
        created (bool): True if the instance was created, False otherwise.
        kwargs (dict): Additional arguments passed to the signal handler.
    """

    if created:

        await send_new_order_message(instance.id)
