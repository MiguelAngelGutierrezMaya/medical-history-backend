"""Deparment serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """Deparment model serializer."""

    class Meta:
        """Meta class."""
        model = Department
        exclude = ['created', 'modified']
