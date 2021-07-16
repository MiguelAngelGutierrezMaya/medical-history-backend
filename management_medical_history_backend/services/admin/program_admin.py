"""Program models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    """Global Program models admin."""

    list_display = [
        'id',
        'description'
    ]
    list_filter = [
        'id',
        'description'
    ]
