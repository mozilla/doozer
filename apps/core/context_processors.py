from django.conf import settings
from django.core.urlresolvers import reverse

import waffle


def nav(request):
    menu = {
        'menu' : [
            ('Home', 'home'),
            ('Gallery', 'games.view_list'),
            ('Rules', 'rules'),
            ('Judges', 'judges'),
            ('Prizes', 'prizes'),
            ('Resources', 'resources'),
        ],
        'location' : request.path,
    }
    if not waffle.is_active(request, 'allow_gallery'):
        menu['menu'].pop(1)
    return menu


def global_settings(request):
    return {'settings': settings}
