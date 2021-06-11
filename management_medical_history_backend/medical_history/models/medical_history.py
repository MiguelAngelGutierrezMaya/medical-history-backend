"""Medical History model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class MedicalHistory(AuditModel):
    """Medical History model."""

    name = models.CharField(max_length=100)

    professional = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        """Return medicalHistory's str representation."""
        return self.name
