"""AppointmentPurpose serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.schedules.models import AppointmentPurpose


class AppointmentPurposeSerializer(serializers.ModelSerializer):
    """AppointmentPurpose model serializer."""

    class Meta:
        """Meta class."""
        model = AppointmentPurpose
        exclude = ['created', 'modified']
