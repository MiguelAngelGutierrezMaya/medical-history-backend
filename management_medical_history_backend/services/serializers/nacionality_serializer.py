"""Nacionality serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import Nacionality


class NacionalitySerializer(serializers.ModelSerializer):
    """Nacionality model serializer."""

    class Meta:
        """Meta class."""
        model = Nacionality
        exclude = ['created', 'modified']
