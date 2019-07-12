from django.contrib import admin
from .models import *
from .models import Competition, Category, Segment, Place
# Register your models here.

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Competition)
admin.site.register(Category)
admin.site.register(Segment)
admin.site.register(Place)