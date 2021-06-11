"""Eps serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import Eps


class EpsSerializer(serializers.ModelSerializer):
    """Eps model serializer."""

    class Meta:
        """Meta class."""
        model = Eps
        exclude = ['created', 'modified']
