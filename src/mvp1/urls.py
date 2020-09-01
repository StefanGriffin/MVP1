
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

from django.urls import path, re_path
from emails.views import email_entry_get_view

urlpatterns = [
    path('email/<int:id>/', email_entry_get_view),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT)

