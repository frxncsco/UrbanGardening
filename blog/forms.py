from django import forms
from .models import Post
from .models import Event
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