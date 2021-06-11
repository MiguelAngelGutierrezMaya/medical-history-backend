"""Eps model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class Eps(AuditModel):
    """Eps model."""

    description = models.CharField(max_length=120)

    def __str__(self):
        """Return eps's str representation."""
        return self.description
