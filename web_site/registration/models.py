from django.db import models

# Create your models here.

class MasterClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date_start = models.DateTimeField('date start')
    date_end = models.DateTimeField('date end')

    def __str__(self):
        return self.name

class Entry(models.Model):
    user_id     = models.IntegerField(default=0)