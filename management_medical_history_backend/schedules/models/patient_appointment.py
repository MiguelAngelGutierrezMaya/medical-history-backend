"""PatientAppointment model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class PatientAppointment(AuditModel):
    """PatientAppointment model."""

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='schedules_patient_appointment_user',
        null=False
    )

    appointment = models.ForeignKey(
        'schedules.Appointment',
        on_delete=models.CASCADE,
        related_name='schedules_patient_appointment',
        null=False
    )

    state = models.ForeignKey(
        'services.State',
        on_delete=models.SET_NULL,
        related_name='schedules_patient_appointment_state',
        null=True
    )

    type_request = models.ForeignKey(
        'services.TypeRequest',
        on_delete=models.SET_NULL,
        related_name='schedules_patient_appointment_type_request',
        null=True
    )

    request_datetime = models.DateTimeField(null=False)

    suggested_datetime = models.DateTimeField(null=False)

    patient_appointment_uuid = models.CharField(max_length=120, null=False)

    ips = models.CharField(max_length=120, null=False)

    production_code = models.CharField(max_length=120, null=False)

    sale_document = models.CharField(max_length=120, blank=True, null=True)

    first_time = models.BooleanField()

    programs = models.TextField()

    def __str__(self):
        """Return patient_appointment's str representation."""
        return str(self.appointment)
