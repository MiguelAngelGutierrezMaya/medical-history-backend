"""Schedule model."""

# Django
from management_medical_history_backend.schedules.models import appointment
from management_medical_history_backend.utils.constants import Constants
from django.db import models
from django.utils.translation import gettext_lazy as _

# Utils
from management_medical_history_backend.utils import AuditModel, Constants


class Availability(AuditModel):
    """Schedule model."""

    professional = models.ForeignKey('users.User', on_delete=models.CASCADE)

    weekday = models.CharField(max_length=50, null=True, choices=Constants.WEEK_DAYS)

    weekday_order = models.PositiveSmallIntegerField(null=True)

    start_date = models.DateTimeField(null=True)

    end_date = models.DateTimeField(null=True)

    can_work = models.BooleanField(default=True)

    all_day = models.BooleanField(default=False)

    # appointment_duration = models.PositiveIntegerField()

    def __str__(self):
        """Return availability's str representation."""
        return self.start_date.strftime('%d/%m/%Y %H:%M:%S')
