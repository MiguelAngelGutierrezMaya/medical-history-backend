"""Exam serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import Exam


class ExamSerializer(serializers.ModelSerializer):
    """Exam model serializer."""

    class Meta:
        """Meta class."""
        model = Exam
        exclude = ['created', 'modified']
