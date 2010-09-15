from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('games.views',
    url(r'^$', 'view_list', name='games.view_list'),
    url(r'^create', 'create', name='games.create'),
    url(r'^(?P<game_id>\d+)$', 'view', name='games.view'),
    url(r'^(?P<game_id>\d+)/edit', 'edit', name='games.edit'),
    url(r'^(?P<game_id>\d+)/delete', 'delete', name='games.delete'),
)
