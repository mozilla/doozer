from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('games.views',
    url(r'^$', 'view_list', name='games.view_list'),
    url(r'^create', 'create', name='games.create'),
    url(r'^edit/(?P<game_id>\d+)$', 'edit', name='games.edit'),
    url(r'^delete/(?P<game_id>\d+)$', 'delete', name='games.delete'),
    url(r'^(?P<game_id>\d+)/(?P<slug>[\w-]+)?', 'view', name='games.view'),
)
