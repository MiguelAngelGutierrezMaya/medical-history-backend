"""Specialist serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import Specialist


class SpecialistSerializer(serializers.ModelSerializer):
    """Specialist model serializer."""

    class Meta:
        """Meta class."""
        model = Specialist
        exclude = ['created', 'modified']
