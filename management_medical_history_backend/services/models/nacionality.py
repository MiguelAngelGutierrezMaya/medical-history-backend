"""Nacionality model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class Nacionality(AuditModel):
    """Nacionality model."""

    code = models.PositiveIntegerField()
    description = models.CharField(max_length=120)

    def __str__(self):
        """Return nacionality's str representation."""
        return self.description
