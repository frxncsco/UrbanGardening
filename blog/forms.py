from django import forms
from .models import Post
from .models import Event
from .models import Comment #KOMMENTAR
from .models import Message #Message
from bootstrap_datepicker_plus import DateTimePickerInput 


class PostForm(forms.ModelForm):

    class Meta:
         model = Post
         fields = ('titel', 'text','bild', 'ort', 'alter') #Felder für Titel, Text, Alter, Bild, Ort als Formular angelegt

######################
#      EVENT         #
######################


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class EventForm(forms.ModelForm):

    class Meta:
         model = Event
         fields = ('eventtitel','beschreibung','veranstaltungsort', 'veranstaltungsdatum', 'uhrzeit')
         widgets = {
            'veranstaltungsdatum': DateInput(), 
            'uhrzeit': TimeInput(),
        }

######################
#      Kommentar     #
######################

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'kommentartext')

######################
#      Message    #
######################

class ContactForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('name', 'email', 'nachricht')
