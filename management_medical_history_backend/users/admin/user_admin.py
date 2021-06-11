"""User models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Global User models admin."""

    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'is_verified',
        'role',
    ]
    list_filter = [
        'id',
        'first_name',
        'last_name',
        'email',
        'is_verified',
        'role',
        'created',
        'modified'
    ]
