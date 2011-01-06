from functools import wraps

from django.conf import settings
from django.http import Http404
from django.utils.decorators import available_attrs


def enabled_or_404(flag):
    """Either a view is enabled, or it's a 404."""
    def decorator(view):
        @wraps(view)
        def _wrapped(request, *args, **kwargs):
            if not getattr(settings, flag):
                raise Http404()
            return view(request, *args, **kwargs)
        return _wrapped
    return decorator
