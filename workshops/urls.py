from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^user/', include('user_profile.urls')),
                       url(r'^workshops/', include('workshop.urls')),
                       url(r'^suggestions/', include('suggestion.urls')),
                       url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('core.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)