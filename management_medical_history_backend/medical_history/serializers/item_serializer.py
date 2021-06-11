"""Item serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.medical_history.models import Item

# Serializer
from management_medical_history_backend.medical_history.serializers import ComponentSerializer


class ItemSerializer(serializers.ModelSerializer):
    """Item model serializer."""

    id = serializers.IntegerField(required=False)

    component = ComponentSerializer()

    class Meta:
        """Meta class."""
        model = Item
        fields = [
            'id',
            'compactType',
            'mounted',
            'i',
            'x',
            'y',
            'w',
            'h',
            'component',
        ]
