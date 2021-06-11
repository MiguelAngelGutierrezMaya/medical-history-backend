"""RelationshipPersonInCharge model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class RelationshipPersonInCharge(AuditModel):
    """RelationshipPersonInCharge model."""

    description = models.CharField(max_length=120)

    def __str__(self):
        """Return relationshipPersonInCharge's str representation."""
        return self.description
