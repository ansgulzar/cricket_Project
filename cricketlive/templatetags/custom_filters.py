from django import template
import re
from django import template
from urllib.parse import unquote

register = template.Library()


@register.filter
def before_by(value):
    pattern = r'By:[^0-9]+[0-9]+\s*hour[s]*\s*ago'
    return re.sub(pattern, '', value).strip()


@register.filter
def urldecode(value):
    return unquote(value)


@register.filter(name='get_nth_value')
def get_nth_value(dictionary, n):
    values = list(dictionary.values())
    if 0 <= n < len(values):
        return values[n]
    return None

# Below code is attached with above code please write in html django template language code it display code as outer loop run inner loop also run on same no of iteration I mean if 4th no of iteration run then inner 4th no iteration run also not 4 time only 4 no of iteration
# {{ images|get_nth_value:forloop.counter0|default:"Value not found" }}
# {{ forloop.counter }} it counter outer loop from 1
# {{ forloop.counter0 }} it counter outer loop from 0


# @register.filter(name='get_nth_value')
# def get_nth_value(dictionary, n):
#     values = list(dictionary.values())
#     if 0 <= n < len(values):
#         return values[n]
#     return None

#  Below code is attached with above code please write in html django template language code you can change the value 1 or 2 or 3 any as no of images you want
# {{images | get_nth_value: 1}}
