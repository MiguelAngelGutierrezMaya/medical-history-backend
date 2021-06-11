"""RelationshipPersonInCharge serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import RelationshipPersonInCharge


class RelationshipPersonInChargeSerializer(serializers.ModelSerializer):
    """RelationshipPersonInCharge model serializer."""

    class Meta:
        """Meta class."""
        model = RelationshipPersonInCharge
        exclude = ['created', 'modified']
