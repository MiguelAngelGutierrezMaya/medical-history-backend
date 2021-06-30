"""Category model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class Category(AuditModel):
    """Category model."""

    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120, null=True)

    def __str__(self):
        """Return category str representation."""
        return self.name
