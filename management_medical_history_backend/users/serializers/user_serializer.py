"""User serializer."""

# Django REST framework
from rest_framework import serializers

# Model
from management_medical_history_backend.users.models import User, Profile

# Serializer
from management_medical_history_backend.users.serializers import ProfileSerializer


class UserSerializer(serializers.ModelSerializer):
    """User model serializer."""
    profile = ProfileSerializer(required=False)

    def create(self, data):
        profile_data = data.pop('profile')
        user = User.objects.create_user(**data, username=data.get('email'), password=data.get('email'))
        Profile.objects.create(**profile_data, user=user)
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.second_name = validated_data.get('second_name', instance.second_name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.second_surname = validated_data.get('second_surname', instance.second_surname)
        instance.save()
        if validated_data.get('profile') is not None:
            profile_data = validated_data.pop('profile')
            Profile.objects.filter(user=instance).update(**profile_data)

        return instance

    class Meta:
        """Meta class."""
        model = User
        fields = (
            'email',
            'first_name',
            'second_name',
            'surname',
            'second_surname',
            'role',
            'profile',
        )
