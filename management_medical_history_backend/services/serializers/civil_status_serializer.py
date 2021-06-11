"""CivilStatus serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import CivilStatus


class CivilStatusSerializer(serializers.ModelSerializer):
    """CivilStatus model serializer."""

    class Meta:
        """Meta class."""
        model = CivilStatus
        exclude = ['created', 'modified']
