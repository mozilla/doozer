from django.core.urlresolvers import reverse

def nav(request):
    return {
        'menu' : [
            ('Competition Home', 'home'),
            ('Rules', 'rules'),
            ('Judges', 'judges'),
            ('Prizes', 'prizes'),
            ('Resources', 'resources'),
        ],
        'location' : request.path,
    }