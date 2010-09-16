from django.shortcuts import render_to_response
from django.template import RequestContext


def render(request, template, data=None, mimetype=None):
    c = RequestContext(request)
    return render_to_response(template, data, c, mimetype=mimetype)
