"""UserMedicalHistory serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.medical_history.models import (
    UserMedicalHistory
)

# serializer
from management_medical_history_backend.users.serializers import UserSerializer
from management_medical_history_backend.medical_history.serializers import MedicalHistorySerializer


class UserMedicalHistorySerializer(serializers.ModelSerializer):
    """UserMedicalHistorySerializer model serializer."""

    user = UserSerializer(read_only=True)
    medical_history = MedicalHistorySerializer(read_only=True)

    def create(self, data):
        return data

    def update(self, instance, validated_data):
        # print(validated_data)
        return instance

    class Meta:
        """Meta class."""
        model = UserMedicalHistory
        fields = ['date', 'professional', 'user', 'medical_history']
