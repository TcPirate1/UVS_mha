from django import template
import datetime

register = template.Library()

@register.filter(name='add_label_class')
def add_label_class(field, css_class):
    return field.label_tag(attrs={'class': css_class})

@register.simple_tag
def current_year():
    return datetime.datetime.now().year