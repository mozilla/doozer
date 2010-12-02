from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('games.views',
    # no gallery yet!
    url(r'^$', 'view_list', name='games.view_list'),
    url(r'^(?P<game_id>\d+)/(?P<slug>[\w-]+)?', 'view', name='games.view'),
    url(r'^mine$', 'mine', name='games.mine'),
    url(r'^create', 'create', name='games.create'),
    url(r'^edit/(?P<game_id>\d+)$', 'edit', name='games.edit'),
    url(r'^delete/(?P<game_id>\d+)$', 'delete', name='games.delete'),
    url(r'^screenshots/(?P<game_id>\d+)$', 'screenshots',
        name='games.screenshots'),
    url(r'^screenshots/(?P<game_id>\d+)/delete/(?P<screenshot_id>\d+)$',
        'screenshot_delete', name='games.screenshot_delete')
)
