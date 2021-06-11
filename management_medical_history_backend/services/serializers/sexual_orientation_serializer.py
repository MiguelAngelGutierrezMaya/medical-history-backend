"""SexualOrientation serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import SexualOrientation


class SexualOrientationSerializer(serializers.ModelSerializer):
    """SexualOrientation model serializer."""

    class Meta:
        """Meta class."""
        model = SexualOrientation
        exclude = ['created', 'modified']
