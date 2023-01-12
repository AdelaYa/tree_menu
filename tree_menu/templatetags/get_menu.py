from django import template
from django.conf import settings
from tree_menu.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu.html')
def draw_menu(name):
    menu_items = MenuItem.objects.filter(
        menu_name__name = name,
    )
    return {
        "menu_items": menu_items,
    }