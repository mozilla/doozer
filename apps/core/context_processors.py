from django.core.urlresolvers import reverse

def nav(request):
    return {
        'menu' : [
            ('Competition Home', 'home'),
            ('How It Works', 'how'),
            ('Rules', 'rules'),
            ('Judges', 'judges'),
            ('Prizes', 'prizes'),
            ('Resources', 'resources'),
        ],
        'location' : request.path,
    }