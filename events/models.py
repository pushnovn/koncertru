from django.db import models

# Create your models here.
class EventPlace(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to='static/events_images')
    age_restriction = models.CharField(max_length=2)
    place = models.ForeignKey(EventPlace)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    event = models.ForeignKey(Event)
    price = models.IntegerField()
    place = models.IntegerField()
    type = models.CharField(max_length=3)
    sector = models.CharField(max_length=3, blank=True)
    row = models.IntegerField(blank=True)

    def __str__(self):
        return '{} (тип: {}, цена: {}, место: {})'.format(self.event, self.type, self.price, self.place)
