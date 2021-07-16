"""State models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import State


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    """Global State models admin."""

    list_display = [
        'id',
        'description'
    ]
    list_filter = [
        'id',
        'description'
    ]
