from django.conf.urls.defaults import patterns, url

from vote import views


urlpatterns = patterns('',
    url(r'^$', views.ballot, name='vote.ballot'),
    url(r'^/vote$', views.vote, name='vote.vote'),
)
