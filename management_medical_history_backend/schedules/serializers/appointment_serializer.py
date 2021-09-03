"""Appointment serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.schedules.models import Appointment
from management_medical_history_backend.users.serializers import ProfileSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    """Appointment model serializer."""

    class Meta:
        """Meta class."""
        model = Appointment
        exclude = ['created', 'modified']


class FullAppointmentSerializer(serializers.ModelSerializer):
    """FullAppointmentSerializer model serializer."""

    patient = ProfileSerializer(read_only=True)

    class Meta:
        """Meta class."""
        model = Appointment
        fields = [
            'id',
            'appointment_duration',
            'created',
            'description',
            'end_date',
            'modified',
            'patient',
            'professional_id',
            'start_date',
            'status',
            'title'
        ]
