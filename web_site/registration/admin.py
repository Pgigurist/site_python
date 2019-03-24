from django.contrib import admin

from .models import MasterClass, Entry
# Register your models here.

class MasterClassAdmin(admin.ModelAdmin):
    listDisplay = ('name', 'date_start', 'date_end') 
    inLine = [Entry]

admin.site.register(MasterClass, MasterClassAdmin)
admin.site.register(Entry)

