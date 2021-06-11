"""HcOpenPlace serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import HcOpenPlace


class HcOpenPlaceSerializer(serializers.ModelSerializer):
    """HcOpenPlace model serializer."""

    class Meta:
        """Meta class."""
        model = HcOpenPlace
        exclude = ['created', 'modified']
