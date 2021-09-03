"""PatientAppointment serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.schedules.models import PatientAppointment

# Serializers
from management_medical_history_backend.users.serializers import UserSerializer
from management_medical_history_backend.services.serializers import (TypeRequestSerializer, StateSerializer)
from management_medical_history_backend.schedules.serializers import FullAppointmentSerializer


class PatientAppointmentSerializer(serializers.ModelSerializer):
    """PatientAppointment model serializer."""

    class Meta:
        """Meta class."""
        model = PatientAppointment
        exclude = ['created', 'modified']


class FullPatientAppointmentSerializer(serializers.ModelSerializer):
    """FullPatientAppointmentSerializer model serializer."""

    user = UserSerializer(read_only=True)
    type_request = TypeRequestSerializer(read_only=True)
    state = StateSerializer(read_only=True)
    appointment = FullAppointmentSerializer(read_only=True)

    class Meta:
        """Meta class."""
        model = PatientAppointment
        fields = [
            'id',
            'appointment',
            'created',
            'first_time',
            'ips',
            'modified',
            'patient_appointment_uuid',
            'production_code',
            'programs',
            'request_datetime',
            'sale_document',
            'type_request',
            'suggested_datetime',
            'user',
            'state'
        ]
