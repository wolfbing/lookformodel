from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^profile$', views.business_profile, name="business_profile"),
    url(r'^create$', views.order_create, name="order_create"),
    url(r'^manage$', views.order_manage, name="order_manage"),
    url(r'^order$', views.order_detail, name="order_detail"),
    url(r'^collect$', views.collect, name="collect"),
)