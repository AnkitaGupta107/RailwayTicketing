from __future__ import unicode_literals

from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)


class Train(models.Model):
    train_name = models.CharField(max_length=100)
    source = models.ForeignKey(City, related_name='source_trains')
    destination = models.ForeignKey(City, related_name='destination_trains')
    total_tickets = models.IntegerField(default=100)
    ticket_price = models.DecimalField(decimal_places=2, max_digits=4)


class BookedTicket(models.Model):
    train = models.ForeignKey(Train)
    no_of_tickets = models.IntegerField(default=1)
    amount = models.DecimalField(decimal_places=2, max_digits=4)
