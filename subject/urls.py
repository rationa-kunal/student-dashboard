from django.conf.urls import include, url
from .views import list_links, list_subject, like, dislike


urlpatterns = [
    url(r'(?P<wrapper_id>[0-9]+)/$', list_links, name='list_of_links'),
    url(r'(?P<wrapper_id>[0-9]+)/(?P<link_id>[0-9]+)/like$', like, name='like'),
    url(r'(?P<wrapper_id>[0-9]+)/(?P<link_id>[0-9]+)/dislike$', dislike, name='dislike'),
    url(r'^$', list_subject, name='homepage'),
]