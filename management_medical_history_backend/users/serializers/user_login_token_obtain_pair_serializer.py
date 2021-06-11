"""User Login Token Obtain Pair Serializer."""

# Django REST framework
from rest_framework import serializers

# Django REST framework Simple JWT
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Models
from management_medical_history_backend.users.models import Profile

# Serializer
from management_medical_history_backend.users.serializers import UserSerializer


class UserLoginTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        if(not user.is_verified):
            raise serializers.ValidationError('Account is not active.')
        token = super().get_token(user)

        # Add custom claims
        profile = Profile.objects.get(user=user)
        obj = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'role': user.role,
            'profile': {
                'id': profile.id,
                'phone_number': profile.phone_number,
                'address': profile.address,
                'picture': profile.picture,
                'birthday': profile.birthday,
            }
        }
        token['user'] = UserSerializer(obj).data

        return token
