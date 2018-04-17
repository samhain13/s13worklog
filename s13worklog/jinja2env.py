from jinja2 import Environment

from django.urls import reverse


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'dir': dir,
        'reverse': reverse,
    })
    return env
