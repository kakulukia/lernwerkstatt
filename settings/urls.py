from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from bookings.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
