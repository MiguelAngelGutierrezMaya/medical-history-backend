"""Appointment model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel, Constants


class Appointment(AuditModel):
    """Appointment model."""

    patient = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='schedules_appointment_patient',
        null=True
    )

    professional = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='schedules_appointment_professional',
        null=True
    )

    start_date = models.DateTimeField(null=True)

    end_date = models.DateTimeField(null=True)

    status = models.CharField(choices=Constants.APPOINTMENT_OPTIONS, max_length=80)

    appointment_duration = models.PositiveIntegerField()

    title = models.CharField(max_length=120)

    description = models.TextField()

    def __str__(self):
        """Return appointment's str representation."""
        return str(self.title)
