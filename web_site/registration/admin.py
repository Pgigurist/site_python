from django.contrib import admin
from .models import *
from .models import MasterClass, Entry, User, UserProfileInfo
# Register your models here.


class EntryInline(admin.TabularInline):
    model = Entry

class EntryAdmin(admin.ModelAdmin):
    #list_display = [field.name for field in Entry._meta.fields]
    list_display = ('user_name')

    def user_name(self, obj):
        name = User.objects.filter(self.user_id)
        return name
    inline = [EntryInline]
    search_fields = ['master_class_id', 'user_id'] ###group number add
    #list_filter = ["date_start", 'date_end']#grouip number

class MasterClassAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MasterClass._meta.fields]
   # listDisplay = ('name', 'date_start', 'date_end')
    exclude = ["id"]
    inlines = [EntryInline]
    #search_fields = ['name', 'date_start', 'date_end'] ###subject add
    #list_filter = ["date_start", 'date_end']#subject



admin.site.register(MasterClass, MasterClassAdmin)
admin.site.register(Entry)
admin.site.register(UserProfileInfo)

