"""ItemValue model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class ItemValue(AuditModel):
    """ItemValue model."""

    value = models.CharField(max_length=200)

    # Relations
    item = models.ForeignKey('medical_history.Item', on_delete=models.CASCADE)
    user_medical_history = models.ForeignKey('medical_history.UserMedicalHistory', on_delete=models.CASCADE)

    def __str__(self):
        """Return ItemValue."""
        return self.value
