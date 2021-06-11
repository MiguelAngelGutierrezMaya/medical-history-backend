"""Profile model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel
from management_medical_history_backend.utils import Constants


class Token(AuditModel):
    """Token model."""

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    type = models.CharField(
        max_length=100,
        choices=Constants.TOKEN_TYPES,
    )

    key = models.CharField(max_length=254)

    valid_from = models.DateTimeField(auto_now_add=True)

    valid_until = models.DateTimeField()

    is_available = models.BooleanField(default=True)

    def __str__(self):
        """Return token's str representation."""
        return 'user:' + str(self.user) + ', token: ' + self.key

    class Meta(AuditModel.Meta):
        unique_together = ['type', 'key']
