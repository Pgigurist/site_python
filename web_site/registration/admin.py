from django.contrib import admin
from .models import *
from .models import MasterClass, Entry, User, UserProfileInfo, Camp, Coach, TeamCoaches
# Register your models here.

class ImagesInLine(admin.TabularInline):
    model = MediaImage
    extra = 1

class MediaImageAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'title', 'image_img')
    list_filter = ['pub_date']
    search_fields = ['title']

    def icon_tag(self):
        return u'<img src="%s" />' % self.url



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

class CoachAdmin(admin.ModelAdmin):
    list_display = ['name']


class CampAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_start', 'date_end', 'place']

admin.site.register(MediaImage, MediaImageAdmin)
admin.site.register(MasterClass, MasterClassAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(UserProfileInfo)
admin.site.register(Camp, CampAdmin)
admin.site.register(TeamCoaches)
