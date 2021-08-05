"""Presentation serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import Presentation


class PresentationSerializer(serializers.ModelSerializer):
    """Presentation model serializer."""

    class Meta:
        """Meta class."""
        model = Presentation
        exclude = ['created', 'modified']
