"""Lending model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class Lending(AuditModel):
    """Lending model.
    """

    name = models.CharField(max_length=80, null=False, blank=False)
    address = models.CharField(max_length=80, null=True, blank=True)
    telephone = models.CharField(max_length=80, null=True, blank=True)
    cellphone = models.CharField(max_length=80, null=True, blank=True)

    is_active = models.BooleanField(
        'Active',
        default=True,
        help_text='Set to true when the lending is active.'
    )

    def __str__(self):
        """Return name's str representation."""
        return str(self.name)
