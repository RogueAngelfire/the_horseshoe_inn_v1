from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, number_of_guests):
    return price * number_of_guests
