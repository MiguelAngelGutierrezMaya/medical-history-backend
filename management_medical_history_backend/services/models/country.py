"""Country model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class Country(AuditModel):
    """Country model."""

    code = models.PositiveIntegerField()
    description = models.CharField(max_length=120)

    def __str__(self):
        """Return country's str representation."""
        return self.description
