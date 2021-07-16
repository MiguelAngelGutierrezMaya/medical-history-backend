"""TypeRequest serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import TypeRequest


class TypeRequestSerializer(serializers.ModelSerializer):
    """TypeRequest model serializer."""

    class Meta:
        """Meta class."""
        model = TypeRequest
        exclude = ['created', 'modified']
