"""ProductionCenter model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class ProductionCenter(AuditModel):
    """ProductionCenter model."""

    code = models.CharField(
        'ProductionCenter code',
        unique=True,
        max_length=20
    )
    name = models.CharField(max_length=120)

    def __str__(self):
        """Return ProductionCenter's str representation."""
        return self.name
