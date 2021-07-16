"""Users URLs"""

# Django
from django.urls import path

# Django REST framework
from rest_framework.urlpatterns import format_suffix_patterns

# Django REST framework Simple JWT
from rest_framework_simplejwt.views import TokenRefreshView

# Views
from management_medical_history_backend.users.views import (
    UserLoginTokenObtainPairView,
    ResetPasswordView,
    ConfirmTokenView,
    IndexCardHolderView,
    UserView
)


urlpatterns = [
    path('api/user/', UserView.as_view(), name='user'),
    path('api/login/', UserLoginTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('api/reset-password/confirm/', ConfirmTokenView.as_view(), name='reset_password_confirm'),
    path('api/index-card-holder/', IndexCardHolderView.as_view(), name='index_card_holder'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
