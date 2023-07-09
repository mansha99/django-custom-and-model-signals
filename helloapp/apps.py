from django.apps import AppConfig

class HelloappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "helloapp"
    def ready(self):
        from helloapp import receivers
