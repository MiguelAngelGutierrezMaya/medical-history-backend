"""Appointment models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.schedules.models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """Global Appointment models admin."""

    list_display = [
        'id',
        'title',
        'patient',
        'professional',
        'start_date',
        'end_date',
        'appointment_duration',
        'status'
    ]
    list_filter = [
        'id',
        'title',
        'patient',
        'professional',
        'start_date',
        'end_date',
        'appointment_duration',
        'status'
    ]
