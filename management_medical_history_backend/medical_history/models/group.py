"""Group model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class Group(AuditModel):
    """Group model."""

    name = models.CharField(max_length=100)

    title = models.CharField(max_length=100)

    medical_history_id = models.PositiveIntegerField()

    def __str__(self):
        """Return group's str representation."""
        return self.name
