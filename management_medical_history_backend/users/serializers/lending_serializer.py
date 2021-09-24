"""Lending serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.users.models import Lending


class LendingSerializer(serializers.ModelSerializer):
    """Lending model serializer."""

    class Meta:
        """Meta class."""
        model = Lending
        fields = (
            'id',
            'name',
            'address',
            'telephone',
            'cellphone'
        )
