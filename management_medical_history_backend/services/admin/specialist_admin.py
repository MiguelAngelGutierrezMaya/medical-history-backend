"""Specialist models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import Specialist


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    """Global Specialist models admin."""

    list_display = [
        'id',
        'description'
    ]
    list_filter = [
        'id',
        'description'
    ]
