from django.apps import AppConfig


class Leave2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EMS'
    # Preserve original migration/app label so existing migrations continue to work
    label = 'EMS'
