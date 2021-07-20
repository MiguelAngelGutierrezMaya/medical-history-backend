"""PatientAppointment serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.schedules.models import PatientAppointment


class PatientAppointmentSerializer(serializers.ModelSerializer):
    """PatientAppointment model serializer."""

    class Meta:
        """Meta class."""
        model = PatientAppointment
        exclude = ['created', 'modified']
