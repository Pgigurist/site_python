from datetime import date
import django
from django.db import models
########
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

    def __str__(self):
        return self.user.username


class MasterClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date_start = models.DateTimeField(default=django.utils.timezone.now)
    subject = models.Case()
    # availiable_seats = models.Count(default=50) ####после регистрации каждого участика будет -1
    date_end = models.DateTimeField(default=django.utils.timezone.now)
    verbose_name_plural = "stories"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


    def __str__(self):
        return self.name


class Entry(models.Model):
    user_id = models.PositiveIntegerField(default=0)
    master_class_id = models.ForeignKey(MasterClass, models.CASCADE)
   # group_id = models.PositiveIntegerField(default=0)
    verbose_name = "Заявка"
    verbose_name_plural = "Заявки на участиe"


    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки на участие"




