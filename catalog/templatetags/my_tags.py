from django import template


register = template.Library()


@register.filter()
def mediapath(value) -> str:
    if value:
        return f'/media/{value}'
    return '/media/default.jpg'

@register.simple_tag()
def mediafile(value) ->str:
    if value:
        return f'/media/{value}'
    return '/media/default.jpg'
