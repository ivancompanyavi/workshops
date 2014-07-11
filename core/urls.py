from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'core.views.home', name='home'),
                       url(r'^admin/', include(admin.site.urls)),
)
