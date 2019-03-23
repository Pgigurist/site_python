from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.MKList, name='index'),
    url(r'(?P<MasterClass_id>\d+)/$', views.masterClassDetalis, name='detalis'),
]
