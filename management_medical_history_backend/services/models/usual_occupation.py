"""UsualOccupation model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class UsualOccupation(AuditModel):
    """UsualOccupation model."""

    description = models.CharField(max_length=120)

    def __str__(self):
        """Return usualOccupation's str representation."""
        return self.description
