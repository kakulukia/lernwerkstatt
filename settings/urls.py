from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from bookings.views import index, show_page, BookingView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    path('buchung', BookingView.as_view()),
    path('<slug:name>', show_page),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
