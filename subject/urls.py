from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r's/$', views.list_subject, name='homepage'),
    url(r's/link/(?P<link_id>[0-9]+)/$', views.link_detail, name='link_detail'),
    url(r's/(?P<wrapper_id>[0-9]+)/$', views.list_links, name='list_of_links'),
    url(r's/(?P<wrapper_id>[0-9]+)/add_link$', views.list_links, name='add_link'),
    url(r's/(?P<wrapper_id>[0-9]+)/(?P<link_id>[0-9]+)/like$', views.like, name='like'),
    url(r's/(?P<wrapper_id>[0-9]+)/(?P<link_id>[0-9]+)/dislike$', views.dislike, name='dislike'),url(r'$', views.greeting, name='greeting'),
]