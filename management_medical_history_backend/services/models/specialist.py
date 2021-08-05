"""Specialist model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class Specialist(AuditModel):
    """Specialist model."""

    description = models.CharField(max_length=120)

    def __str__(self):
        """Return specialis's str representation."""
        return self.description
