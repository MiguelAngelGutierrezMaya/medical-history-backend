"""Exam models admin."""

# Django
from django.contrib import admin

# Model
from management_medical_history_backend.services.models import Exam


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    """Global Exam models admin."""

    list_display = [
        'id',
        'description'
    ]
    list_filter = [
        'id',
        'description'
    ]
