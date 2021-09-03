"""Users views."""

# Django REST Framework
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from management_medical_history_backend.medical_history.models import (
    MedicalHistory,
    UserMedicalHistory,
    Group,
    Item,
    ItemValue,
    Component,
    user_medical_history,
)

# Serializers
from management_medical_history_backend.medical_history.serializers import (
    MedicalHistorySerializer,
    UserMedicalHistorySerializer,
    UserMedicalHistorySignUpSerializer,
    ItemValueSerializer,
    MedicalHistorySimpleSerializer,
)


class MedicalHistoryConfigView(APIView):
    def post(self, request):
        """Handle HTTP POST request."""
        serializer = MedicalHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """Handle HTTP GET request."""
        list = MedicalHistory.objects.all()
        serializer = MedicalHistorySimpleSerializer(list, many=True)
        return Response(serializer.data)


class MedicalHistoryConfigDetailView(APIView):
    def get(self, request, hc_id):
        """Handle HTTP GET request."""
        try:
            hc = MedicalHistory.objects.get(id=hc_id)
            groups = Group.objects.filter(medical_history_id=hc.id)
            data = {
                'id': hc.id,
                'name': hc.name,
                'groups': groups
            }
            aux_groups = []
            for group in groups:
                items = Item.objects.filter(group=group)
                aux_groups.append({
                    'id': group.id,
                    'name': group.name,
                    'title': group.title,
                    'items': items,
                })
            data['groups'] = aux_groups

            serializer = MedicalHistorySerializer(data)
            return Response(serializer.data)
        except MedicalHistory.DoesNotExist:
            return Response({'msg': 'No se econtró la Historia Clínica solicitada'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, hc_id):
        try:
            hc = MedicalHistory.objects.get(id=hc_id)
            serializer = MedicalHistorySerializer(hc, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MedicalHistory.DoesNotExist:
            return Response({'msg': 'No se econtró la Historia Clínica solicitada'}, status=status.HTTP_400_BAD_REQUEST)


class ReportUserMedicalHistoryView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        kws = {'user__profile__nuip': request.GET['document']}
        if 'date_init' in request.GET:
            kws['date__gte'] = request.GET['date_init']
        if 'date_end' in request.GET:
            kws['date__lte'] = request.GET['date_end']
        list = UserMedicalHistory.objects.filter(**kws)
        serializer = UserMedicalHistorySerializer(list, many=True)
        return Response(serializer.data)


class UserMedicalHistoryView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        list = UserMedicalHistory.objects.filter(user_id=request.GET['user_id'])
        serializer = UserMedicalHistorySerializer(list, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Handle HTTP POST request."""
        serializer = UserMedicalHistorySignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserMedicalHistoryDetailView(APIView):
    def get(self, request, umh_id):
        """Handle HTTP GET request."""
        try:
            umh = UserMedicalHistory.objects.get(id=umh_id)
            itemsValue = ItemValue.objects.filter(user_medical_history=umh)
            serializer = ItemValueSerializer(itemsValue, many=True)
            return Response(serializer.data)
        except UserMedicalHistory.DoesNotExist:
            return Response({'msg': 'No se econtró la Historia Clínica de usuario solicitada'}, status=status.HTTP_400_BAD_REQUEST)
