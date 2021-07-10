"""Nacionality models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import Nacionality


@admin.register(Nacionality)
class NacionalityAdmin(admin.ModelAdmin):
    """Global Nacionality models admin."""

    list_display = [
        'id',
        'code',
        'description'
    ]
    list_filter = [
        'id',
        'code',
        'description'
    ]
