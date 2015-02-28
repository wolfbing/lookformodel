from django.conf.urls import patterns, include, url
from django.contrib import admin

from lookformodel import views as lkm_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'JiaxingMedia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r"^hello/$", lkm_views.hello),
)
