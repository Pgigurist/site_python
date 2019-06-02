from django.db import models
from django.core.validators import URLValidator

# Create your models here.

class Competition(models.Model):
    name = models.CharField(max_length=100)
    annonce = models.TextField()
    liveVideoLink = models.TextField(validators=[URLValidator()])
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
