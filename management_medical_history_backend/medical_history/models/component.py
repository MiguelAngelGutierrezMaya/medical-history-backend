"""Component model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class Component(AuditModel):
    """Component model."""

    type = models.CharField(max_length=80)

    label = models.CharField(max_length=80)

    item = models.OneToOneField('medical_history.Item', on_delete=models.CASCADE)

    def __str__(self):
        """Return component's str representation."""
        return self.label
