"""User models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Global Profile models admin."""

    list_display = [
        'id',
        'user',
        'phone_number',
        'address',
    ]
    list_filter = [
        'id',
        'user',
        'phone_number',
        'address',
        'created',
        'modified'
    ]
