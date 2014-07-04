from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^workshops/', 'webapp.views.workshops', name='workshops'),
    url(r'^login/', 'webapp.views.make_login', name='login'),
    url(r'^logout/', 'webapp.views.make_logout', name='logout'),
    url(r'^register/', 'webapp.views.register', name='register'),
    url(r'^profile/', 'webapp.views.profile', name='profile'),
    url(r'^change_avatar/', 'webapp.views.change_avatar', name='change_avatar'),
    url(r'^create_workshop/', 'webapp.views.create_workshop', name='create_workshop'),
    url(r'^workshop_detail/(?P<workshop_id>\d+)/?$', 'webapp.views.workshop_detail', name='workshop_detail'),
    url(r'^workshop_subscribe/(?P<workshop_id>\d+)/?$', 'webapp.views.workshop_subscribe', name='workshop_subscribe'),
    url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)