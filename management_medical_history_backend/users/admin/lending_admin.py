"""Lending models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.users.models import Lending


@admin.register(Lending)
class LendingAdmin(admin.ModelAdmin):
    """Global User models admin."""

    list_display = [
        'id',
        'name',
        'address',
        'cellphone',
        'telephone',
        'is_active'
    ]
    list_filter = [
        'id',
        'name'
    ]
