"""User login TokenObtainPairView"""

# Django REST framework Simple JWT
from rest_framework_simplejwt.views import TokenObtainPairView

# Serializers
from management_medical_history_backend.users.serializers import UserLoginTokenObtainPairSerializer


class UserLoginTokenObtainPairView(TokenObtainPairView):
    """User login TokenObtainPairView"""
    serializer_class = UserLoginTokenObtainPairSerializer
