"""Ips serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import Ips


class IpsSerializer(serializers.ModelSerializer):
    """Ips model serializer."""

    class Meta:
        """Meta class."""
        model = Ips
        exclude = ['created', 'modified']
