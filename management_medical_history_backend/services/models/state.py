"""State model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class State(AuditModel):
    """State model."""

    description = models.CharField(max_length=120)

    def __str__(self):
        """Return State str representation."""
        return self.description
