from django.contrib import admin
from .models import Post
from .models import Event
from .models import Comment #KOMMENTAR
from .models import Kontakt #KONTAKT

admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Comment) #KOMMENTAR
admin.site.register(Kontakt) #KONTAKT

