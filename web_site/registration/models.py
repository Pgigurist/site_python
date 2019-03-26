from django.db import models
from django.contrib import admin
# Create your models here.

class MasterClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    #date_start = models.DateTimeField()
    #date_end = models.DateTimeField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    user_id = models.PositiveIntegerField(default=0)
    master_class_id = models.ForeignKey(MasterClass, models.CASCADE)
    verbose_name_plural = "Master Classes"
