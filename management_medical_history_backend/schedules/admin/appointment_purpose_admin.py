"""AppointmentPurpose models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.schedules.models import AppointmentPurpose


@admin.register(AppointmentPurpose)
class AppointmentPurposeAdmin(admin.ModelAdmin):
    """Global AppointmentPurpose models admin."""

    list_display = [
        'id',
        'description'
    ]
    list_filter = [
        'id',
        'description'
    ]
