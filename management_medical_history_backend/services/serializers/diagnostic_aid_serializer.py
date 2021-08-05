"""DiagnosticAid serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import DiagnosticAid


class DiagnosticAidSerializer(serializers.ModelSerializer):
    """DiagnosticAid model serializer."""

    class Meta:
        """Meta class."""
        model = DiagnosticAid
        exclude = ['created', 'modified']
