"""Department models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Global Department models admin."""

    list_display = [
        'id',
        'code',
        'description',
        'country_id'
    ]
    list_filter = [
        'id',
        'code',
        'description',
        'country_id'
    ]
