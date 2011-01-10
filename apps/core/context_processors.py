from django.core.urlresolvers import reverse

def nav(request):
    return {
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