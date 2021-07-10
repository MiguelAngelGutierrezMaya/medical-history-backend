"""City models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Global City models admin."""

    list_display = [
        'id',
        'code',
        'description',
        'department_id'
    ]
    list_filter = [
        'id',
        'code',
        'description',
        'department_id'
    ]
