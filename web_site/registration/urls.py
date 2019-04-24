from django.conf.urls import url
from . import views

#SET NAMESPACE  чтобы не писать через точку
app_name = 'registration'

urlpatterns = [
    url(r'^list/$', views.MKList, name='mk_list'), #MK list
    url(r'^(?P<mk_id>[0-9]+)/$', views.MKDetalis, name='mk_id'),#MK detalis
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
