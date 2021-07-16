"""Program serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import Program


class ProgramSerializer(serializers.ModelSerializer):
    """Program model serializer."""

    class Meta:
        """Meta class."""
        model = Program
        exclude = ['created', 'modified']
