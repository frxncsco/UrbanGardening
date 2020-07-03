from django.contrib import admin
from .models import Post
from .models import Event

admin.site.register(Post)
admin.site.register(Event)