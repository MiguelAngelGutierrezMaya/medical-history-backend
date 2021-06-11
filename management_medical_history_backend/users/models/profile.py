"""Profile model."""

# Django
from django.db import models

# Utils
from management_medical_history_backend.utils import AuditModel


class Profile(AuditModel):
    """Profile model.

    A profile a holds a user's public data like biography and picture."""

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=80, null=False, blank=True)

    picture = models.ImageField(
        'Profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    # Tab One
    surname = models.CharField(max_length=80, null=True, blank=True)
    second_surname = models.CharField(max_length=80, null=True, blank=True)
    first_name = models.CharField(max_length=80, null=True, blank=True)
    second_name = models.CharField(max_length=80, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=80, null=True, blank=True)
    nuip = models.CharField(max_length=80, null=True, blank=True)
    nationality = models.ForeignKey('services.Nacionality', on_delete=models.CASCADE, null=True)
    country = models.ForeignKey('services.Country', on_delete=models.CASCADE, null=True)
    department = models.ForeignKey('services.Department', on_delete=models.CASCADE, null=True)
    city = models.ForeignKey('services.City', on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=80, null=True, blank=True)
    neighborhood = models.CharField(max_length=120, null=True, blank=True)
    telephone = models.CharField(max_length=80, null=True, blank=True)
    cellphone = models.CharField(max_length=80, null=True, blank=True)
    usual_occupation = models.CharField(max_length=120, null=True, blank=True)
    special_population = models.CharField(max_length=80, null=True, blank=True)
    sexual_orientation = models.CharField(max_length=80, null=True, blank=True)
    social_security_scheme = models.CharField(max_length=80, null=True, blank=True)
    eps = models.CharField(max_length=120, null=True, blank=True)
    eps_level = models.CharField(max_length=20, null=True, blank=True)
    affiliation_number = models.CharField(max_length=100, null=True, blank=True)

    # Tab Two
    civil_status = models.CharField(max_length=80, null=True, blank=True)
    scholarship = models.CharField(max_length=100, null=True, blank=True)
    ethnic_group = models.CharField(max_length=120, null=True, blank=True)
    type_degree_disability = models.CharField(max_length=80, null=True, blank=True)
    work_address = models.CharField(max_length=20, null=True, blank=True)
    work_phone_one = models.CharField(max_length=20, null=True, blank=True)
    work_phone_two = models.CharField(max_length=20, null=True, blank=True)
    last_name_mom = models.CharField(max_length=80, null=True, blank=True)
    first_name_mom = models.CharField(max_length=80, null=True, blank=True)
    responsable = models.CharField(max_length=120, null=True, blank=True)
    relationship_person_in_charge = models.CharField(max_length=100, null=True, blank=True)
    address_person_in_charge = models.CharField(max_length=80, null=True, blank=True)
    telephone_person_in_charge = models.CharField(max_length=80, null=True, blank=True)

    # Tab Three
    hc_open_place = models.CharField(max_length=120, null=True, blank=True)
    user_create_hc = models.CharField(max_length=80, null=True, blank=True)
    hc_transfer_to = models.CharField(max_length=120, null=True, blank=True)
    transfer_date = models.DateField(null=True, blank=True)
    date_last_attention = models.DateField(null=True, blank=True)
    user_alert = models.CharField(max_length=120, null=True, blank=True)
    user_message_hc = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
