"""Deparment model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class Department(AuditModel):
    """Deparment model."""

    code = models.PositiveIntegerField()
    description = models.CharField(max_length=120)
    country = models.ForeignKey('services.Country', on_delete=models.CASCADE)

    def __str__(self):
        """Return deparment's str representation."""
        return self.description
