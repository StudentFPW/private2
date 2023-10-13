from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    """
    Он берет строку и заменяет все экземпляры данной подстроки другой подстрокой.

    :param context: Контекст текущей страницы
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    # Кодирование словаря в строку запроса URL.
    return d.urlencode()
