from django.conf.urls import include, url
from .views import list_links, list_subject


urlpatterns = [
    url(r'(?P<wrapper_id>[0-9]+)/$', list_links, name='list_of_links'),
    url(r'^$', list_subject, name='homepage'),
]