"""Diagnose model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class Diagnose(AuditModel):
    """Diagnose model."""

    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120, null=True)

    def __str__(self):
        """Return diagnose str representation."""
        return self.name
