"""TypeRequest models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import TypeRequest


@admin.register(TypeRequest)
class TypeRequestAdmin(admin.ModelAdmin):
    """Global TypeRequest models admin."""

    list_display = [
        'id',
        'description'
    ]
    list_filter = [
        'id',
        'description'
    ]
