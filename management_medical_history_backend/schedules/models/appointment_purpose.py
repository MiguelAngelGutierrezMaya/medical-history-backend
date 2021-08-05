"""AppointmentPurpose model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class AppointmentPurpose(AuditModel):
    """AppointmentPurpose model."""

    description = models.CharField(max_length=120)

    def __str__(self):
        """Return appointment_purpose's str representation."""
        return self.description
