"""TypeDegreeDisability model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class TypeDegreeDisability(AuditModel):
    """TypeDegreeDisability model."""

    description = models.CharField(max_length=120)

    def __str__(self):
        """Return typeDegreeDisability's str representation."""
        return self.description
