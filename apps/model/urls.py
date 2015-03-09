from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.model_list, name="model_list"),
    url(r'^detail/$', views.model_detail, name="model_detail"),
    url(r'^album/$', views.model_album, name="model_album"),
    url(r'^album/photo/$', views.model_photo, name="model_photo"),
    url(r'^notice/$', views.model_notice, name="model_notice"),
)