from django.core.urlresolvers import reverse

def nav(request):
    return {
        'menu' : [
            ('Competition Home', 'home'),
            ('Rules', 'rules'),
            ('Judging', 'judging'),
            ('Prizes', 'prizes'),
            ('Resources', 'resources'),
        ],
        'location' : request.path,
    }