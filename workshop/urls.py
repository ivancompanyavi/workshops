from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^new/?', 'workshop.views.workshop_new', name='workshop_new'),
                       url(r'^(?P<workshop_id>\d+)/?$', 'workshop.views.workshop_detail',
                           name='workshop_detail'),
                       url(r'^(?P<workshop_id>\d+)/subscribe/?$', 'workshop.views.workshop_subscribe',
                           name='workshop_subscribe'),
                       url(r'^(?P<workshop_id>\d+)/questions/new/?$', 'workshop.views.question_new',
                           name='question_new'),
                       url(r'^(?P<workshop_id>\d+)/questions/(?P<question_id>\d+)/?$', 'workshop.views.question_detail',
                           name='question_detail'),
                       url(r'^/?$', 'workshop.views.workshops', name='workshop_list'),
                       url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)