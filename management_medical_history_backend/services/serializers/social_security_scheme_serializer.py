"""SocialSecurityScheme serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.services.models import SocialSecurityScheme


class SocialSecuritySchemeSerializer(serializers.ModelSerializer):
    """SocialSecurityScheme model serializer."""

    class Meta:
        """Meta class."""
        model = SocialSecurityScheme
        exclude = ['created', 'modified']
