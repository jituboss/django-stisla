import hashlib
from datetime import datetime, timezone
from django.template import Library

register = Library()

@register.filter(name='logged_in')
def logged_in(value):
    return ((datetime.now(timezone.utc) - value).seconds % 3600) // 60

@register.filter(name='md5')
def md5(value):
    return hashlib.md5(value.encode()).hexdigest()