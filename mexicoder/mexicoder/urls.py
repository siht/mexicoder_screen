from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mexicoder.views.home', name='home'),
    url(r'^screen/', include('screen.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
