"""City model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class City(AuditModel):
    """City model."""

    code = models.PositiveIntegerField()
    description = models.CharField(max_length=120)
    department = models.ForeignKey('services.Department', on_delete=models.CASCADE)

    def __str__(self):
        """Return city's str representation."""
        return self.description
