from datetime import date
import django
from django.db import models
########
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
# Create your models here.
class MediaImage(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateField('date published', null=True)
    image = models.ImageField(upload_to='static/uploads/img', null=True)
    
    def image_img(self):
        if self.image:
            return mark_safe(u'<img src="/{0}" width="100"/>'.format(self.image.url))
        else:
            return '(none)'

    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __str__(self):
        return "[%d] %s" % (self.id, self.title)
        #return self.image_img
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
    description = models.TextField()
    locationX = models.CharField(max_length=100)
    locationY = models.CharField(max_length=100)
    locationZoom = models.CharField(max_length=10)
    
    def camp_map(self):
        return mark_safe(u'<script src="https://api-maps.yandex.ru/2.1/?lang=ru_RU&amp;apikey=0bd996a4-badf-46ed-b4fc-748760a4da64" type="text/javascript"></script><div id="campMap" width="200" height="200"></div><script>let campMap; ymaps.ready(init); function init(){let api="0bd996a4-badf-46ed-b4fc-748760a4da64"; myMap = new ymaps.Map("campMap",{center:[55.032697,44.493349],zoom:13},{searchControlProvider:"yandex#search"})}</script>')
    camp_map.short_description = 'карта'
    camp_map.allow_tags = True

    class Meta:
        verbose_name = "Сборы"
        verbose_name_plural = "Сборы"
    def __str__(self):
        return self.name

class Coach(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    mediaImage = models.ForeignKey(MediaImage, models.CASCADE, default=None)

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренера"
    def __str__(self):
        return self.name


class TeamCoaches(models.Model):
    camp = models.ForeignKey(Camp, models.CASCADE)
    coach = models.ForeignKey(Coach, models.CASCADE)

    def __str__(self):
        return self.camp.name


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


