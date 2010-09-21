from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.inclusion_tag("navigation.html", takes_context=True)
def navigation(context):
    m = []
    for name, path in context['menu']:
        m.append((name, reverse(path)))
    context['menu'] = m
    return context
