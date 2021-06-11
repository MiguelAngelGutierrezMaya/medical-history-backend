"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utils
from management_medical_history_backend.utils import AuditModel, Constants


class User(AuditModel, AbstractUser):
    """Users model.

    Extends from Django's AbstractUser, change the username field
    to email and add some extra fields."""

    first_name = models.CharField(max_length=50, null=True)

    second_name = models.CharField(max_length=50, null=True)

    surname = models.CharField(max_length=80, null=True, blank=False)

    second_surname = models.CharField(max_length=80, null=True, blank=False)

    email = models.EmailField(
        'Email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exist.'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_verified = models.BooleanField(
        'Verified',
        default=True,
        help_text='Set to true when the user have verified email address.'
    )

    role = models.CharField(
        max_length=30,
        choices=Constants.ROLE_OPTIONS,
        default=Constants.ROLE_ADMIN,
    )

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username
