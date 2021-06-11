# Django REST framework
from rest_framework import permissions

# Models
from management_medical_history_backend.users.models import User


class AccessPermission(permissions.BasePermission):
    """Veried that the user is authenticated"""
    message = 'Don\'t has permission to access.'

    def has_permission(self, request, view):
        user = User.objects.get(pk=request.user.id)
        if (user is None or user.is_verified is False):
            return False
        else:
            return True
