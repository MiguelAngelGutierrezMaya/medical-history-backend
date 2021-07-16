"""Services URL"""

# Django
from django.urls import path

# Django REST framework
from rest_framework.urlpatterns import format_suffix_patterns

# Views
from management_medical_history_backend.schedules.views import (
    ScheduleRecordsView,
    AvailabilitiesRecordsView,
    AvailabilitiesView,
    RescheduleDetailView,
)


urlpatterns = [
    path('api/availabilities/', AvailabilitiesRecordsView.as_view(), name='availabilities'),
    path('api/user-availabilities/', AvailabilitiesView.as_view(), name='user_availabilities'),
    path('api/schedules/', ScheduleRecordsView.as_view(), name='schedules'),
    path('api/reschedule/', RescheduleDetailView.as_view(), name='schedules'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
