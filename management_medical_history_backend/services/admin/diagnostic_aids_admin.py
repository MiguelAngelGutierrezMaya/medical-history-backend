"""DiagnosticAid models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import DiagnosticAid


@admin.register(DiagnosticAid)
class DiagnosticAidAdmin(admin.ModelAdmin):
    """Global DiagnosticAid models admin."""

    list_display = [
        'id',
        'description'
    ]
    list_filter = [
        'id',
        'description'
    ]
