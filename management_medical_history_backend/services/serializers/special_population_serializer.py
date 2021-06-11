"""SpecialPopulation serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import SpecialPopulation


class SpecialPopulationSerializer(serializers.ModelSerializer):
    """SpecialPopulation model serializer."""

    class Meta:
        """Meta class."""
        model = SpecialPopulation
        exclude = ['created', 'modified']
