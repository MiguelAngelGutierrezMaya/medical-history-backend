"""ProductionCenter serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import ProductionCenter


class ProductionCenterSerializer(serializers.ModelSerializer):
    """ProductionCenter model serializer."""

    class Meta:
        """Meta class."""
        model = ProductionCenter
        exclude = ['created', 'modified']
