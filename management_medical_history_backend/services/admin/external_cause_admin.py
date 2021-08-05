"""ExternalCause models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import ExternalCause


@admin.register(ExternalCause)
class ExternalCauseAdmin(admin.ModelAdmin):
    """Global ExternalCause models admin."""

    list_display = [
        'id',
        'description'
    ]
    list_filter = [
        'id',
        'description'
    ]
