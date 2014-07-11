from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^login/', 'user_profile.views.make_login', name='login'),
                       url(r'^logout/', 'user_profile.views.make_logout', name='logout'),
                       url(r'^register/', 'user_profile.views.register', name='register'),
                       url(r'^profile/', 'user_profile.views.profile', name='profile'),
                       url(r'^change_avatar/', 'user_profile.views.change_avatar', name='change_avatar'),
                       url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
