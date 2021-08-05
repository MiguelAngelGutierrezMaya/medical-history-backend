"""Medicine serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import Medicine


class MedicineSerializer(serializers.ModelSerializer):
    """Medicine model serializer."""

    class Meta:
        """Meta class."""
        model = Medicine
        exclude = ['created', 'modified']
