"""Category serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Category model serializer."""

    class Meta:
        """Meta class."""
        model = Category
        exclude = ['created', 'modified']
