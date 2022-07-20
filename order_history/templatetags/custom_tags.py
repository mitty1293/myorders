from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.simple_tag
def get_type(object):
    return type(object)


@register.simple_tag
def get_vars(object):
    return vars(object)


@register.filter
@stringfilter
def addstr(value, arg):
    return value + arg
