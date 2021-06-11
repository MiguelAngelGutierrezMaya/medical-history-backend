"""Scholarship serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import Scholarship


class ScholarshipSerializer(serializers.ModelSerializer):
    """Scholarship model serializer."""

    class Meta:
        """Meta class."""
        model = Scholarship
        exclude = ['created', 'modified']
