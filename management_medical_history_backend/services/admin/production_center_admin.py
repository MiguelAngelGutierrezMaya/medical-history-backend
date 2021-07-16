"""ProductionCenter models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import ProductionCenter


@admin.register(ProductionCenter)
class ProductionCenterAdmin(admin.ModelAdmin):
    """Global ProductionCenter models admin."""

    list_display = [
        'id',
        'code',
        'name'
    ]
    list_filter = [
        'id',
        'code',
        'name'
    ]
