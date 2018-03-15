from django.contrib import admin
from .models import Subject, LinkWrapper, Link, Tag


admin.site.register(Subject)
admin.site.register(Link)
admin.site.register(LinkWrapper)
admin.site.register(Tag)


