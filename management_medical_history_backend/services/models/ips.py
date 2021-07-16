"""Ips model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class Ips(AuditModel):
    """Ips model."""

    code = models.CharField(
        'Ips code',
        unique=True,
        max_length=20
    )
    name = models.CharField(max_length=120)

    def __str__(self):
        """Return Ips's str representation."""
        return self.name
