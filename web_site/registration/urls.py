from django.conf.urls import url
from . import views

#SET NAMESPACE
app_name = 'registration'

urlpatterns = [
    url(r'^list/$', views.MKList, name='mk_list'), #mkList
    url(r'^(?P<mk_id>[0-9]+)/$', views.MKDetalis, name='mk_id'),#mk detalis
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    #url(r'^landing/$', views.Landing, name='landing'),
    #url(r'^$', views.index, name='index'),#index page,
]
