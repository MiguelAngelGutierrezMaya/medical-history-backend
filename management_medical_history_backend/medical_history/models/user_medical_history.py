"""UserMedicalHistory model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class UserMedicalHistory(AuditModel):
    """UserMedicalHistory model."""

    date = models.DateTimeField(null=False)

    # Relations
    professional = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, related_name='%(class)s_professional')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='%(class)s_user')
    medical_history = models.ForeignKey('medical_history.MedicalHistory', on_delete=models.CASCADE)

    def __str__(self):
        """Return UserMedicalHistory."""
        return self.user
