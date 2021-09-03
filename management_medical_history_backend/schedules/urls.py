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
    PatientAppointmentView,
    AppointmentPurposeView,
    ReportPatientAppointmentView
)


urlpatterns = [
    path('api/availabilities/', AvailabilitiesRecordsView.as_view(), name='availabilities'),
    path('api/user-availabilities/', AvailabilitiesView.as_view(), name='user_availabilities'),
    path('api/patient-appointments/', PatientAppointmentView.as_view(), name='patient_appointments'),
    path('api/appointment-purposes/', AppointmentPurposeView.as_view(), name='appointment_purposes'),
    path('api/report-appointments/', ReportPatientAppointmentView.as_view(), name='report-appointments'),
    path('api/schedules/', ScheduleRecordsView.as_view(), name='schedules'),
    path('api/reschedule/', RescheduleDetailView.as_view(), name='schedules'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
