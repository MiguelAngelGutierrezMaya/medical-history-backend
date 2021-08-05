"""Medicine models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import Medicine


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    """Global Medicine models admin."""

    list_display = [
        'id',
        'description'
    ]
    list_filter = [
        'id',
        'description'
    ]
