from django.db import models

# Create your models here.
class EventPlace(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()


class Event(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to='static/events_images')
    age_restriction = models.CharField(max_length=2)
    place = models.ForeignKey(EventPlace)


class Ticket(models.Model):
    event = models.ForeignKey(Event)
    price = models.IntegerField()
