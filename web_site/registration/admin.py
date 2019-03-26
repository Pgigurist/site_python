from django.contrib import admin

from .models import MasterClass, Entry
# Register your models here.

class MasterClassAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MasterClass._meta.fields]
   # listDisplay = ('name', 'date_start', 'date_end')
    inLine = [Entry]

admin.site.register(MasterClass, MasterClassAdmin)
admin.site.register(Entry)

