"""State serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import State


class StateSerializer(serializers.ModelSerializer):
    """State model serializer."""

    class Meta:
        """Meta class."""
        model = State
        exclude = ['created', 'modified']
