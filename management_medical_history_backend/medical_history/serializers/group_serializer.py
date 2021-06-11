"""Group serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.medical_history.models import Group

# Serializer
from management_medical_history_backend.medical_history.serializers import ItemSerializer


class GroupSerializer(serializers.ModelSerializer):
    """Group model serializer."""

    id = serializers.IntegerField(required=False)

    items = ItemSerializer(many=True, required=False)

    class Meta:
        """Meta class."""
        model = Group
        fields = ['id', 'name', 'title', 'items']
