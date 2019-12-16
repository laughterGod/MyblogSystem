from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'
    verbose_name = '用户'

    def ready(self):
        super(UserConfig, self).ready()
        from . import signals