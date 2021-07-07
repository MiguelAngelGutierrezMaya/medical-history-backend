"""ItemValue serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.medical_history.models import ItemValue

# Serializer
from management_medical_history_backend.medical_history.serializers import UserMedicalHistorySerializer
from management_medical_history_backend.medical_history.serializers import ItemSerializer


class ItemValueSerializer(serializers.ModelSerializer):
    """ItemValue model serializer."""

    user_medical_history = UserMedicalHistorySerializer(read_only=True)
    item = ItemSerializer(read_only=True)

    class Meta:
        """Meta class."""
        model = ItemValue
        fields = [
            'value',
            'type',
            'item',
            'user_medical_history'
        ]
