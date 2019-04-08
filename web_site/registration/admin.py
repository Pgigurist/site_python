from django.contrib import admin
from .models import *
from .models import MasterClass, Entry
# Register your models here.
<<<<<<< HEAD
# admin.site.register(Entry)
=======

class MasterClassAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MasterClass._meta.fields]
   # listDisplay = ('name', 'date_start', 'date_end')
    exclude = ["id"]
    inLine = [Entry]
    #search_fields = ['name', 'date_start', 'date_end'] ###subject add
    #list_filter = ["date_start", 'date_end']#subject

class EntryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Entry._meta.fields]
   # listDisplay = ('name', 'date_start', 'date_end')
    inLine = [Entry]
    search_fields = ['master_class_id', 'user_id'] ###group number add
    #list_filter = ["date_start", 'date_end']#grouip number


admin.site.register(MasterClass, MasterClassAdmin)
admin.site.register(Entry)
>>>>>>> stage_one

class MasterClassAdmin(admin.ModelAdmin):
    fieldsets = [
        ('basic', {'fields': ['name', 'description']}),
    ]

admin.site.register(MasterClass, MasterClassAdmin)

class EntryAdmin(admin.ModelAdmin):
    filds = ['master_class']
admin.site.register(Entry, EntryAdmin )
