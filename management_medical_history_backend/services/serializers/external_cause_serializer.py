"""ExternalCause serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import ExternalCause


class ExternalCauseSerializer(serializers.ModelSerializer):
    """ExternalCause model serializer."""

    class Meta:
        """Meta class."""
        model = ExternalCause
        exclude = ['created', 'modified']
