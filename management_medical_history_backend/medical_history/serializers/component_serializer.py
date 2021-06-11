"""Component serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.medical_history.models import Component


class ComponentSerializer(serializers.ModelSerializer):
    """Component model serializer."""

    id = serializers.IntegerField(required=False)

    class Meta:
        """Meta class."""
        model = Component
        fields = ['id', 'type', 'label']
