from django import template

register = template.Library()
@register.filter
def to_and(value):
    return value.split('/')


#@register.filter
#def chart(value):

