"""UsualOccupation serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import UsualOccupation


class UsualOccupationSerializer(serializers.ModelSerializer):
    """UsualOccupation model serializer."""

    class Meta:
        """Meta class."""
        model = UsualOccupation
        exclude = ['created', 'modified']
