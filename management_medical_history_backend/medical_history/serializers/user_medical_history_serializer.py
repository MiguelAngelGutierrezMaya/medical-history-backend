"""UserMedicalHistory serializer."""

# Django REST framework
from management_medical_history_backend.medical_history import models
from rest_framework import serializers

# Model
from management_medical_history_backend.medical_history.models import (
    UserMedicalHistory,
    ItemValue
)

# serializer
from management_medical_history_backend.users.serializers import UserSerializer
from management_medical_history_backend.medical_history.serializers import MedicalHistorySimpleSerializer


class UserMedicalHistorySerializer(serializers.ModelSerializer):
    """UserMedicalHistorySerializer model serializer."""

    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    professional = UserSerializer(read_only=True)
    medical_history = MedicalHistorySimpleSerializer(read_only=True)

    class Meta:
        """Meta class."""
        model = UserMedicalHistory
        fields = ['id', 'date', 'professional', 'user', 'medical_history']


class UserMedicalHistorySignUpSerializer(serializers.ModelSerializer):
    """UserMedicalHistorySignUpSerializer model serializer."""

    itemsValue = serializers.ListField()
    diagnosesCategories = serializers.ListField()
    specialists = serializers.ListField()
    diagnosticAids = serializers.ListField()
    medicines = serializers.ListField()
    exams = serializers.ListField()
    date = serializers.DateTimeField()
    medical_history_id = serializers.IntegerField()
    professional_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    appointmentPurpose = serializers.CharField()
    externalCause = serializers.CharField()

    def create(self, data):
        aux = data
        itemsValue = data.pop('itemsValue')
        diagnosesCategories = data.pop('diagnosesCategories')
        specialists = data.pop('specialists')
        diagnosticAids = data.pop('diagnosticAids')
        medicines = data.pop('medicines')
        exams = data.pop('exams')
        appointmentPurpose = data.pop('appointmentPurpose')
        externalCause = data.pop('externalCause')
        user_medical_history = UserMedicalHistory.objects.create(**data)

        ItemValue.objects.create(
            value=appointmentPurpose,
            type='appointmentPurposes',
            user_medical_history_id=user_medical_history.id
        )
        ItemValue.objects.create(
            value=externalCause,
            type='externalCauses',
            user_medical_history_id=user_medical_history.id
        )

        for diagnoseCategory in diagnosesCategories:
            ItemValue.objects.create(
                value=diagnoseCategory,
                type='diagnosesCategories',
                user_medical_history_id=user_medical_history.id
            )
        for specialist in specialists:
            ItemValue.objects.create(
                value=specialist,
                type='specialists',
                user_medical_history_id=user_medical_history.id
            )
        for diagnosticAid in diagnosticAids:
            ItemValue.objects.create(
                value=diagnosticAid,
                type='diagnosticAids',
                user_medical_history_id=user_medical_history.id
            )
        for medicine in medicines:
            ItemValue.objects.create(
                value=medicine,
                type='medicines',
                user_medical_history_id=user_medical_history.id
            )
        for exam in exams:
            ItemValue.objects.create(
                value=exam,
                type='exams',
                user_medical_history_id=user_medical_history.id
            )
        for itemValue in itemsValue:
            ItemValue.objects.create(
                value=itemValue['value'],
                type='itemValue',
                item_id=itemValue['item']['id'],
                user_medical_history_id=user_medical_history.id
            )

        aux['itemsValue'] = itemsValue
        aux['diagnosesCategories'] = diagnosesCategories
        aux['specialists'] = specialists
        aux['diagnosticAids'] = diagnosticAids
        aux['medicines'] = medicines
        aux['exams'] = exams
        aux['appointmentPurpose'] = appointmentPurpose
        aux['externalCause'] = externalCause
        return aux

    class Meta:
        """Meta class."""
        model = UserMedicalHistory
        fields = (
            'itemsValue',
            'diagnosesCategories',
            'specialists',
            'diagnosticAids',
            'medicines',
            'exams',
            'appointmentPurpose',
            'externalCause',
            'date',
            'medical_history_id',
            'professional_id',
            'user_id'
        )
