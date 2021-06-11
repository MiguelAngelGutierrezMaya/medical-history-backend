"""Scholarship model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class Scholarship(AuditModel):
    """Scholarship model."""

    description = models.CharField(max_length=120)

    def __str__(self):
        """Return scholarship's str representation."""
        return self.description
