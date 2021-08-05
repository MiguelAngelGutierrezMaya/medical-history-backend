"""Presentation models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import Presentation


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    """Global Presentation models admin."""

    list_display = [
        'id',
        'description'
    ]
    list_filter = [
        'id',
        'description'
    ]
