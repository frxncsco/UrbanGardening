from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titel = models.CharField(max_length=200)
    text = models.TextField()
    alter = models.CharField (max_length=10)#Anlage der Variable Alter mit entsprechendem Eingabefeld
    bild = models.ImageField(default='images/default.jpg', upload_to= 'images/', blank = True ) #Anlage der Variable Bild mit entsprechendem Eingabefeld
    ort = models.CharField(max_length=100)#Anlage der Variable Ort mit entsprechendem Eingabefeld
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titel

class Event(models.Model):
    eventtitel= models.CharField(max_length=200)
    beschreibung = models.TextField()
    veranstaltungsort = models.CharField(max_length=100)
    published_date2 = models.DateTimeField(blank=True, null=True)
    veranstaltungsdatum = models.DateField()
  

    def publish(self):
        self.published_date2 = timezone.now()
        self.save()

    def __str__(self):
        return self.eventtitel
