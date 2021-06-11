"""HcOpenPlace model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class HcOpenPlace(AuditModel):
    """HcOpenPlace model."""

    description = models.CharField(max_length=120)

    def __str__(self):
        """Return hcOpenPlace's str representation."""
        return self.description
