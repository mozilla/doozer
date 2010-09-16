from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext


def render(request, template, data=None, mimetype=None):
    """Render a template with a RequestContext."""
    c = RequestContext(request)
    return render_to_response(template, data, c, mimetype=mimetype)
