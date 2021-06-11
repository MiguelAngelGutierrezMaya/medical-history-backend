"""Users URLs"""

# Django
from django.urls import path

# Django REST framework
from rest_framework.urlpatterns import format_suffix_patterns

# Views
from management_medical_history_backend.medical_history.views import (
    MedicalHistoryConfigView,
    MedicalHistoryConfigDetailView,
)


urlpatterns = [
    path('api/medical-history-config/', MedicalHistoryConfigView.as_view(), name='medical_history_config'),
    path('api/medical-history-config-detail/<int:hc_id>',
         MedicalHistoryConfigDetailView.as_view(), name='medical_history_config_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
