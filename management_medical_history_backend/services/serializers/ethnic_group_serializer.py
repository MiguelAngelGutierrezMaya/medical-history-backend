"""EthnicGroup serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import EthnicGroup


class EthnicGroupSerializer(serializers.ModelSerializer):
    """EthnicGroup model serializer."""

    class Meta:
        """Meta class."""
        model = EthnicGroup
        exclude = ['created', 'modified']
