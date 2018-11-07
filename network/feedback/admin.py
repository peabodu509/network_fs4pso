from __future__ import unicode_literals
from django.contrib import admin
from .models import Post, Subject, Comment, Like

admin.site.register(Post)
admin.site.register(Subject)
admin.site.register(Comment)
admin.site.register(Like)