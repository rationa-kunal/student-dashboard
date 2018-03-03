from django.contrib import admin
from .models import Subject, LinkWrapper, Link


admin.site.register(Subject)
admin.site.register(Link)
admin.site.register(LinkWrapper)


