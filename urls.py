from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/', include('registration.urls')),
    (r'^games/', include('games.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', direct_to_template, {'template': 'base.html'}, name='home'),
    url(r'^how$', direct_to_template, {'template': 'how.html'}, name='how'),
    url(r'^rules$', direct_to_template, {'template': 'rules.html'}, name='rules'),
    url(r'^prizes$', direct_to_template, {'template': 'prizes.html'}, name='prizes'),
    url(r'^judges$', direct_to_template, {'template': 'judges.html'}, name='judges'),
    url(r'^resources$', direct_to_template, {'template': 'resources.html'}, name='resources'),
)

if settings.DEBUG:
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
          {'document_root': settings.MEDIA_ROOT}),
    )
