"""Country serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import Country


class CountrySerializer(serializers.ModelSerializer):
    """Country model serializer."""

    class Meta:
        """Meta class."""
        model = Country
        exclude = ['created', 'modified']
