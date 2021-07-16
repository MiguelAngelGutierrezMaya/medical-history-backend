"""Ips models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import Ips


@admin.register(Ips)
class IpsAdmin(admin.ModelAdmin):
    """Global Ips models admin."""

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
