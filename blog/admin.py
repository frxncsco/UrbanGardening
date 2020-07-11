from django.contrib import admin
from .models import Post
from .models import Event #EVENT
from .models import Comment #KOMMENTAR
from .models import Message #Message

admin.site.register(Post)
admin.site.register(Event) #EVENT
admin.site.register(Comment) #KOMMENTAR
admin.site.register(Message) #Message

