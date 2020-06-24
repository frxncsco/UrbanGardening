from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
         model = Post
         fields = ('titel', 'text','bild', 'ort', 'alter') #Felder für Titel, Text, Alter, Bild, Ort als Formular angelegt
