from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Filtro para obtener un elemento de un diccionario por clave"""
    return dictionary.get(key)

@register.filter
def time_format(time_obj, format_str):
    """Filtro para formatear objetos de tiempo"""
    if time_obj:
        return time_obj.strftime(format_str)
    return "" 