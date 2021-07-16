"""Availability models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.schedules.models import Availability


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    """Global Availability models admin."""

    list_display = [
        'id',
        'professional',
        'weekday',
        'start_date',
        'end_date',
        'appointment_duration'
    ]
    list_filter = [
        'id',
        'professional',
        'weekday',
        'start_date',
        'end_date',
        'appointment_duration'
    ]
