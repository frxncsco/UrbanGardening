from django import forms
from .models import Post
from .models import Event
from .models import Comment #KOMMENTAR
from .models import Kontakt #KONTAKT
from bootstrap_datepicker_plus import DateTimePickerInput


class PostForm(forms.ModelForm):

    class Meta:
         model = Post
         fields = ('titel', 'text','bild', 'ort', 'alter') #Felder für Titel, Text, Alter, Bild, Ort als Formular angelegt


class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(forms.ModelForm):

    class Meta:
         model = Event
         fields = ('eventtitel','beschreibung','veranstaltungsort', 'veranstaltungsdatum')
         widgets = {
            'veranstaltungsdatum': DateInput(), 
        }

######################
#      Kommentar     #
######################

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

######################
#      Kontakt     #
######################

class ContactForm(forms.ModelForm):

    class Meta:
        model = Kontakt
        fields = ('name', 'email', 'nachricht')