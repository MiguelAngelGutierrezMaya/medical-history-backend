"""TypeDegreeDisability serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import TypeDegreeDisability


class TypeDegreeDisabilitySerializer(serializers.ModelSerializer):
    """TypeDegreeDisability model serializer."""

    class Meta:
        """Meta class."""
        model = TypeDegreeDisability
        exclude = ['created', 'modified']
