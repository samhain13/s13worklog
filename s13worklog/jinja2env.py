from jinja2 import Environment

from django.conf import settings
from django.contrib import messages
from django.urls import reverse


def static(*path):
    return settings.STATIC_URL + '/'.join(path)


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'get_messages': messages.get_messages,
        'reverse': reverse,
        'static': static,
    })
    return env
