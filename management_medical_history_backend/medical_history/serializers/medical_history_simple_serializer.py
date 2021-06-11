"""MedicalHistory serializer."""

# Django REST framework
from django.db.models import fields
from management_medical_history_backend.medical_history.models.group import Group
from rest_framework import serializers

# Model
from management_medical_history_backend.medical_history.models import (
    MedicalHistory,
    Group,
    Item,
    Component,
)

# serializer
from management_medical_history_backend.medical_history.serializers import GroupSerializer


class MedicalHistorySimpleSerializer(serializers.ModelSerializer):
    """MedicalHistory model serializer."""

    class Meta:
        """Meta class."""
        model = MedicalHistory
        fields = ['id', 'name', 'professional']
