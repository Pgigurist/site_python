from datetime import date
import django
from django.db import models
########
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    #надстройка над стандартным классом USERMODEL, берет все теже поля что и в user(наследование)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

    def __str__(self):
        return self.user.username

class Camp(models.Model):
    date_start = models.DateField(default=django.utils.timezone.now)
    date_end = models.DateField(default=django.utils.timezone.now)
    place = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Сборы"
        verbose_name_plural = "Сборы"
    def __str__(self):
        return self.name

class Coach(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренера"
    def __str__(self):
        return self.name

class MasterClass(models.Model):
    camp = models.ForeignKey(Camp, models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    subject = models.Case()# что это?
    date_end = models.DateField(default=django.utils.timezone.now)
    date_start = models.DateField(default=django.utils.timezone.now)
    seats = models.PositiveSmallIntegerField(default=15)
    isAvalable = models.BooleanField(default=True)# флаг для закрытия подачи заявок

    def incrimentSeat(self):
        if self.isAvalable:
            self.seats = self.seats-1
            if self.seats < 1:
                self.isAvalable = False
            self.save()
            return True
        else:
            return False

    def decrimentSeat(self):
        self.seats = self.seats+1
        self.save()

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
    

    def __str__(self):
        return self.name


class Entry(models.Model):
    user_id = models.ForeignKey(User, models.CASCADE)#models.PositiveIntegerField(default=0)
    master_class_id = models.ForeignKey(MasterClass, models.CASCADE)
   # group_id = models.PositiveIntegerField(default=0)
    verbose_name = "Заявка"
    verbose_name_plural = "Заявки на участиe"


    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки на участие"

    def __str__(self):
        text = self.master_class_id.name
        return text


