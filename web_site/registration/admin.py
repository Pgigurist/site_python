from django.contrib import admin

from .models import MasterClass, Entry
# Register your models here.
# admin.site.register(Entry)

class MasterClassAdmin(admin.ModelAdmin):
    fieldsets = [
        ('basic', {'fields': ['name', 'description']}),
    ]

admin.site.register(MasterClass, MasterClassAdmin)

class EntryAdmin(admin.ModelAdmin):
    filds = ['master_class']
admin.site.register(Entry, EntryAdmin )
