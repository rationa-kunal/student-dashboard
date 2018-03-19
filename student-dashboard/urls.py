from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.url'), name="accounts"),
    url(r'^', include('subject.urls')),
]
