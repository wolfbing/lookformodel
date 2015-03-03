from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$',views.model_list,name="model_list"),
    url(r'^detail/$',views.model_detail,name="model_detail"),
)