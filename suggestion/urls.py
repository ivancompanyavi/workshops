from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^add/?$', 'suggestion.views.suggestion_add', name='suggestion_add'),
                       url(r'^(?P<suggestion_id>\d+)/delete/?$', 'suggestion.views.suggestion_delete', name='suggestion_delete'),
                       url(r'^$', 'suggestion.views.suggestion_list', name='suggestion_list'),

)
