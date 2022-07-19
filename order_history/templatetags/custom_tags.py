from django import template
from django.db import models

register = template.Library()


@register.simple_tag
def get_vars(object):
    object_vars = vars(object)
    del object_vars["_state"]
    return object_vars
