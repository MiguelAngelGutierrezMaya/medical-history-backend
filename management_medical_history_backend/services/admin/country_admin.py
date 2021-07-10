"""Country models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """Global Country models admin."""

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
