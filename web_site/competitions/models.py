from django.db import models

# Create your models here.

class Competition(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Соревнование"
        verbose_name_plural = "Соревнования"

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=110)
    gender = models.CharField(max_length=1)
    limits = models.PositiveSmallIntegerField(default=18)
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __str__(self):
        return self.name

class Segment(models.Model): 
    name = models.CharField(max_length=110)
    def __str__(self):
        return self.name
