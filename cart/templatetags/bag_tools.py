from django import template


register = template.Library()

@register.filter(name='sum_subtotal')
def sum_subtotal(price, quantity):
    return price * quantity