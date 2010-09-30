from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/', include('registration.urls')),
    (r'^games/', include('games.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', direct_to_template, {'template': 'static/home.html'}, name='home'),
    url(r'^how$', direct_to_template, {'template': 'static/how.html'}, name='how'),
    url(r'^rules$', direct_to_template, {'template': 'static/rules.html'}, name='rules'),
    url(r'^fineprint$', direct_to_template, {'template': 'static/fineprint.html'}, name='fineprint'),
    url(r'^prizes$', direct_to_template, {'template': 'static/prizes.html'}, name='prizes'),
    url(r'^judging$', direct_to_template, {'template': 'static/judging.html'}, name='judging'),
    url(r'^resources$', direct_to_template, {'template': 'static/resources.html'}, name='resources'),
)

if settings.DEBUG:
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
          {'document_root': settings.MEDIA_ROOT}),
    )
