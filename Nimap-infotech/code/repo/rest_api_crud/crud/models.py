from django.db import models

# Create your models here.
from datetime import datetime
from django.utils.timezone import now


class Event(models.Model):
    class StateChoice(models.TextChoices):
        Maharashtra = 'Maharashtra'
        Punjab= 'Punjab'
        Rajasthan='Rajasthan'
        Uttarakhand = 'Uttarakhand'
        Arunachal_Pradesh = 'Arunachal Pradesh'
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50,choices=StateChoice.choices,default=StateChoice.Maharashtra)
    zipcode = models.CharField(max_length=10)
    other = models.CharField(max_length=50)
    start_date = models.CharField(max_length=25)
    end_date = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    list_date = models.DateTimeField(default=now,blank=True)

    class Meta:
        verbose_name_plural = 'events'
    def __str__(self):
        return self.title