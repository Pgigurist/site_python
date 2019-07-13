from django.conf.urls import url
from . import views

#SET NAMESPACE  чтобы не писать через точку
app_name = 'registration'

urlpatterns = [
    url(r'^list/$', views.MKList, name='mk_list'), #MK list
    url(r'^camps/$', views.campList, name="camps"),
    url(r'^campDetalis/([0-9]+)/$', views.campDetalis, name="camp_detalis"),
    url(r'^(?P<mk_id>[0-9]+)/$', views.MKDetalis, name='mk_id'),#MK detalis
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^list/createEntry/$', views.createEntry, name="create_entry"),
    url(r'^list/removeEntry/$', views.removeEntry, name="remove_entry"),
    
]
