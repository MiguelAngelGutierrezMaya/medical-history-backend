"""Development settings."""

from .base import *  # NOQA
from .base import env

# Base
DEBUG = True

# Security
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

# CORS
CORS_ORIGIN_WHITELIST = env.list('DJANGO_CORS_ORIGIN_WHITELIST')

# Static files
STATIC_ROOT = str(ROOT_DIR('/staticfiles'))

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # NOQA

# django-extensions
INSTALLED_APPS += ['django_extensions']  # noqa F405
