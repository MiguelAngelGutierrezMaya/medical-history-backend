"""Diagnose serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import Diagnose


class DiagnoseSerializer(serializers.ModelSerializer):
    """Diagnose model serializer."""

    class Meta:
        """Meta class."""
        model = Diagnose
        exclude = ['created', 'modified']
