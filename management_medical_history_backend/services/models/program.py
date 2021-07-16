"""Program model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class Program(AuditModel):
    """Program model."""

    description = models.CharField(max_length=120)

    def __str__(self):
        """Return Program's str representation."""
        return self.description
