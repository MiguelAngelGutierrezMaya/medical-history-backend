"""Category models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Global Category models admin."""

    list_display = [
        'id',
        'name',
        'description'
    ]
    list_filter = [
        'id',
        'name',
        'description'
    ]
