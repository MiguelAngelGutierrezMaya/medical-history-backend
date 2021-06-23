"""Availability serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.schedules.models import Availability


class AvailabilitySerializer(serializers.ModelSerializer):
    """Availability model serializer."""

    def create(self, data):
        availability = Availability.objects.create(
            weekday=data.get('start_date').strftime('%A').upper(),
            weekday_order=data.get('start_date').weekday(),
            start_date=data.get('start_date'),
            end_date=data.get('end_date'),
            can_work=data.get('can_work'),
            all_day=data.get('all_day', False),
            appointment_duration=data.get('appointment_duration'),
            professional=data.get('professional'),
        )
        return availability

    class Meta:
        """Meta class."""
        model = Availability
        exclude = ['created', 'modified']
