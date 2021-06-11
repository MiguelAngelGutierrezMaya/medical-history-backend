"""MedicalHistory serializer."""

# Django REST framework
from django.db.models import fields
from management_medical_history_backend.medical_history.models.group import Group
from rest_framework import serializers

# Model
from management_medical_history_backend.medical_history.models import (
    MedicalHistory,
    Group,
    Item,
    Component,
)

# serializer
from management_medical_history_backend.medical_history.serializers import GroupSerializer


class MedicalHistorySerializer(serializers.ModelSerializer):
    """MedicalHistory model serializer."""

    groups = GroupSerializer(many=True)

    def create(self, data):
        aux = data
        groups = data.pop('groups')
        medical_history = MedicalHistory.objects.create(**data)
        for group in groups:
            items = group.pop('items')
            new_group = Group.objects.create(**group, medical_history_id=medical_history.id)
            for item in items:
                component = item.pop('component')
                new_item = Item.objects.create(**item, group=new_group)
                Component.objects.create(**component, item=new_item)

        aux['groups'] = groups
        return aux

    def update(self, instance, validated_data):
        # print(validated_data)
        instance.name = validated_data.get('name', instance.name)
        groups = Group.objects.filter(medical_history_id=instance.id)
        groups_validated_data = validated_data.pop('groups')
        for group_validated_data in groups_validated_data:
            items_validated_data = group_validated_data.pop('items')
            if group_validated_data.get('id') is None:
                new_group = Group.objects.create(**group_validated_data, medical_history_id=instance.id)
            else:
                for group in groups:
                    if group_validated_data.get('id') == group.id:
                        group.name = group_validated_data.get('name', group.name)
                        group.title = group_validated_data.get('title', group.title)
                        group.save()
                        new_group = group

            for item_validated_data in items_validated_data:
                items = Item.objects.filter(group=new_group)
                component_validated_data = item_validated_data.pop('component')
                if item_validated_data.get('id') is None:
                    new_item = Item.objects.create(**item_validated_data, group=new_group)
                else:
                    for item in items:
                        if item_validated_data.get('id') == item.id:
                            item.compactType = item_validated_data.get('compactType', item.compactType)
                            item.mounted = item_validated_data.get('mounted', item.mounted)
                            item.i = item_validated_data.get('i', item.i)
                            item.x = item_validated_data.get('x', item.x)
                            item.y = item_validated_data.get('y', item.y)
                            item.w = item_validated_data.get('w', item.w)
                            item.h = item_validated_data.get('h', item.h)
                            item.save()
                            new_item = item
                if component_validated_data.get('id') is None:
                    Component.objects.create(**component_validated_data, item=new_item)

        instance.save()
        validated_data['groups'] = groups_validated_data
        return validated_data

    class Meta:
        """Meta class."""
        model = MedicalHistory
        fields = ['name', 'professional', 'groups']
