from django import template

register = template.Library()


# @register.simple_tag
# def get_verbose_name(instance, field_name):
#     return instance._meta.get_field(field_name).verbose_name.title()


# @register.simple_tag
# def get_all_field_of_model(model):
#     return model._meta.get_fields()[2:]


@register.simple_tag
def get_type(object):
    return type(object)


@register.simple_tag
def get_vars(object):
    return vars(object)
