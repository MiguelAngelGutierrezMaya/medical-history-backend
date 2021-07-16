"""TypeRequest model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class TypeRequest(AuditModel):
    """TypeRequest model."""

    description = models.CharField(max_length=120)

    def __str__(self):
        """Return TypeRequest's str representation."""
        return self.description
