from django.apps import AppConfig
from django.db.models.signals import post_migrate


class OrderHistoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "order_history"

    def ready(self):
        from .models import get_or_create_default

        post_migrate.connect(get_or_create_default, sender=self)
