"""Item model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class Item(AuditModel):
    """Item model."""

    group = models.ForeignKey('medical_history.Group', on_delete=models.CASCADE)

    # Struct UI
    compactType = models.CharField(max_length=80)

    mounted = models.BooleanField()

    i = models.CharField(max_length=80)

    x = models.IntegerField()

    y = models.IntegerField()

    w = models.IntegerField()

    h = models.IntegerField()

    # component = models.OneToOneField('medical_history.Component', on_delete=models.CASCADE)

    def __str__(self):
        """Return component's str representation."""
        return self.compact_type
