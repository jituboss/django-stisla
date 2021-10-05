from django.apps import AppConfig
from django.core.exceptions import ImproperlyConfigured

class admin(AppConfig):
    name = 'django_stisla'

    def ready(self):
        from django.conf import settings
        if 'widget_tweaks' not in settings.INSTALLED_APPS:
            raise ImproperlyConfigured('Please install django-widget-tweaks and add "widget_tweaks" in INSTALLED_APPS!')