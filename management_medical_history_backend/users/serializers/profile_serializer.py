"""User serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""
        model = Profile
        exclude = ['user']
