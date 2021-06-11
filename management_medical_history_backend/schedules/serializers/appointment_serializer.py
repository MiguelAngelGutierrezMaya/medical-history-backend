"""Appointment serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.schedules.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    """Appointment model serializer."""

    class Meta:
        """Meta class."""
        model = Appointment
        exclude = ['created', 'modified']
