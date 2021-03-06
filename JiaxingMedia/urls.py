from django.conf.urls import patterns, include, url
from django.contrib import admin

# from apps.lookformodel import views as lkm_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'JiaxingMedia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r"^$", include('apps.home.urls')),
    url(r"^model/", include('apps.model.urls')),
    url(r"^business/", include('apps.business.urls')),
    url(r"^about/", include('apps.about.urls')),


)
