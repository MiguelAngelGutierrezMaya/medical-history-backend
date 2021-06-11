"""SocialSecurityScheme model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class SocialSecurityScheme(AuditModel):
    """SocialSecurityScheme model."""

    description = models.CharField(max_length=120)

    def __str__(self):
        """Return socialSecurityScheme's str representation."""
        return self.description
