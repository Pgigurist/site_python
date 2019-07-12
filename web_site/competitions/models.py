from django.db import models
from django.core.validators import URLValidator

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=100)
    centerX = models.CharField(max_length=100)
    centerY = models.CharField(max_length=100)
    zoom = models.PositiveSmallIntegerField(default=12)
    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
    def __str__(self):
        return self.name

class Competition(models.Model):
    name = models.CharField(max_length=100)
    annonce = models.TextField()
    liveVideoLink = models.TextField(validators=[URLValidator()])
    place = models.OneToOneField(Place, on_delete=models.CASCADE, blank=True)
    class Meta:
        verbose_name = "Соревнование"
        verbose_name_plural = "Соревнования"

    def __str__(self):
        return self.name
class Category(models.Model):
    competition = models.OneToOneField(Competition, on_delete=models.CASCADE)
    name = models.CharField(max_length=110)
    gender = models.CharField(max_length=1)
    limits = models.PositiveSmallIntegerField(default=18)
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __str__(self):
        return self.name

class Segment(models.Model): 
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=110)
    class Meta:
        verbose_name = "Сегмент"
        verbose_name_plural = "Сегменты"
    def __str__(self):
        return self.name

