from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.about, name="about"),
    url(r'^article/$', views.article_detail, name="article_detail"),
)