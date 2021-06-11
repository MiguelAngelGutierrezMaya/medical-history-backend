"""HcTransferTo serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import HcTransferTo


class HcTransferToSerializer(serializers.ModelSerializer):
    """HcTransferTo model serializer."""

    class Meta:
        """Meta class."""
        model = HcTransferTo
        exclude = ['created', 'modified']
