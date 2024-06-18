# Django imports
from django.apps import AppConfig
from django.core.signals import setting_changed


class OrdersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "order"

    # https://docs.djangoproject.com/en/5.0/topics/signals/#module-django.dispatch
    def ready(self):
        # https://www.geeksforgeeks.org/how-to-create-and-use-signals-in-django/
        import order.signals

