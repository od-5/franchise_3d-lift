from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'', include('apps.landing.urls', namespace='website')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'ticket/', include('apps.ticket.urls', namespace='ticket')),
    url(r'download/', include('apps.download.urls', namespace='download')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
