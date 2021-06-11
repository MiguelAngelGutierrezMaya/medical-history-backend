class Constants:

    # Users
    ROLE_ADMIN = 'ROLE_ADMIN'
    ROLE_PATIENT = 'ROLE_PATIENT'
    ROLE_AUXILIAR = 'ROLE_AUXILIAR'
    ROLE_PROFESSIONAL = 'ROLE_PROFESSIONAL'

    ROLE_OPTIONS = [
        (ROLE_ADMIN, 'Admin role'),
        (ROLE_PATIENT, 'Patient role'),
        (ROLE_AUXILIAR, 'Auxiliar role'),
        (ROLE_PROFESSIONAL, 'Professional role'),
    ]

    # Tokens
    TYPE_ACCOUNT_CONFIRMATION = 'ACCOUNT_CONFIRMATION'
    TYPE_RESET_PASSWORD = 'RESET_PASSWORD'

    TOKEN_TYPES = [
        (TYPE_ACCOUNT_CONFIRMATION, 'Account confirmation'),
        (TYPE_RESET_PASSWORD, 'Reset password')
    ]

    APPOINTMENT_PENDING = 'PENDING'
    APPOINTMENT_PAID = 'PAID'
    APPOINTMENT_FINISHED = 'FINISHED'
    APPOINTMENT_CANCELED = 'CANCELED'

    APPOINTMENT_OPTIONS = [
        (APPOINTMENT_PENDING, 'Appointment pending'),
        (APPOINTMENT_PAID, 'Appointment paid'),
        (APPOINTMENT_FINISHED, 'Appointment finished'),
        (APPOINTMENT_CANCELED, 'Appointment cenceled'),
    ]

    WEEK_DAY_MONDAY = 'MONDAY'
    WEEK_DAY_TUESDAY = 'TUESDAY'
    WEEK_DAY_WEDNESDAY = 'WEDNESDAY'
    WEEK_DAY_THURSDAY = 'THURSDAY'
    WEEK_DAY_FRIDAY = 'FRIDAY'
    WEEK_DAY_SATURDAY = 'SATURDAY'
    WEEK_DAY_SUNDAY = 'SUNDAY'

    WEEK_DAYS = [
        (WEEK_DAY_MONDAY, 'Lunes'),
        (WEEK_DAY_TUESDAY, 'Martes'),
        (WEEK_DAY_WEDNESDAY, 'Miércoles'),
        (WEEK_DAY_THURSDAY, 'Jueves'),
        (WEEK_DAY_FRIDAY, 'Viernes'),
        (WEEK_DAY_SATURDAY, 'Sábado'),
        (WEEK_DAY_SUNDAY, 'Domingo'),
    ]
