from django.core.context_processors import csrf
from django.http import HttpResponse
from django.template import RequestContext, Template
from django.template.loader import get_template


def render(request, template, data=None, mimetype=None, status=200):
    """Render a template with a RequestContext."""
    t = get_template(template)
    c = RequestContext(request, data)
    return HttpResponse(t.render(c), mimetype=mimetype, status=status)
