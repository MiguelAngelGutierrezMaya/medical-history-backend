"""PatientAppointment models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.schedules.models import PatientAppointment


@admin.register(PatientAppointment)
class PatientAppointmentAdmin(admin.ModelAdmin):
    """Global PatientAppointment models admin."""

    list_display = [
        'id',
        'user',
        'appointment',
        'request_datetime',
        'first_time'
    ]
    list_filter = [
        'id',
        'user',
        'appointment',
        'request_datetime',
        'first_time'
    ]
