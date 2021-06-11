"""City serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import City


class CitySerializer(serializers.ModelSerializer):
    """City model serializer."""

    class Meta:
        """Meta class."""
        model = City
        exclude = ['created', 'modified']
