from datetime import date
import django
from django.db import models


# Create your models here.

class MasterClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    date_start = models.DateTimeField(default=django.utils.timezone.now)
    subject = models.Case()
    # availiable_seats = models.Count(default=50) ####после регистрации каждого участика будет -1
    date_end = models.DateTimeField(default=django.utils.timezone.now)
verbose_name_plural = "stories"

class Meta:
    verbose_name = "Master Class"
    verbose_name_plural = "Master Classes"


def __str__(self):
    return self.name



class Entry(models.Model):

    user_id = models.PositiveIntegerField(default=0)
    master_class_id = models.ForeignKey(MasterClass, models.CASCADE)
   # group_id = models.PositiveIntegerField(default=0)
    verbose_name = "Entry"
    verbose_name_plural = "Entries"


class Meta:
    verbose_name = "Entry"
    verbose_name_plural = "Entries"





