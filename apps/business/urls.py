from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'profile^$', views.business_profile, name="business_profile"),
)