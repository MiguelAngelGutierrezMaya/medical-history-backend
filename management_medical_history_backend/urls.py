"""management_medical_history_backend URL Configuration"""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import url

admin.site.site_header = 'Siellano Systems'
admin.site.site_title = 'Administration'
admin.site.index_title = 'Siellano Systems Administration'
admin.autodiscover()

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include(('management_medical_history_backend.users.urls', 'users'), namespace='users')),
    path('', include(('management_medical_history_backend.services.urls', 'services'), namespace='services')),
    path('', include(('management_medical_history_backend.medical_history.urls', 'medical_history'), namespace='medical_history')),
    path('', include(('management_medical_history_backend.schedules.urls', 'schedules'), namespace='schedules')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
