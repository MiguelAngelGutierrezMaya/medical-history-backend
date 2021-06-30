"""Diagnose models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import Diagnose


@admin.register(Diagnose)
class DiagnoseAdmin(admin.ModelAdmin):
    """Global Diagnose models admin."""

    list_display = [
        'id',
        'name',
        'description'
    ]
    list_filter = [
        'id',
        'name',
        'description'
    ]
