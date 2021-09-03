"""Users views."""

# Django REST Framework
from management_medical_history_backend.schedules.models.patient_appointment import PatientAppointment
from re import L
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from management_medical_history_backend.schedules.models import (
    Availability,
    Appointment,
    AppointmentPurpose,
    PatientAppointment
)
from management_medical_history_backend.users.models import User

# Serializers
from management_medical_history_backend.schedules.serializers import (
    AvailabilitySerializer,
    AppointmentSerializer,
    PatientAppointmentSerializer,
    AppointmentPurposeSerializer,
    FullPatientAppointmentSerializer
)

# Utils
from management_medical_history_backend.utils.permissions import AccessPermission
from management_medical_history_backend.utils import Constants
from datetime import datetime, timedelta
from django.utils import timezone, dateformat


class AvailabilitiesRecordsView(APIView):
    """List professional's availabilities"""
    permission_classes = [permissions.IsAuthenticated, AccessPermission]

    def get(self, request):
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        except Exception:
            return Response('Fechas no válida', status=status.HTTP_400_BAD_REQUEST)

        availabilities = Availability.objects.filter(
            start_date__gte=start_date,
            end_date__lte=(end_date + timedelta(days=1)),
            professional=request.user
        ).order_by('weekday_order', 'start_date')
        serializer = AvailabilitySerializer(availabilities, many=True)
        return Response(serializer.data)

    def put(self, request):
        """Handle HTTP PUT request."""
        for i in range(0, len(request.data)):
            request.data[i]['professional'] = request.user.id
            if request.data[i].get('id') is not None:
                availability = Availability.objects.get(pk=request.data[i].get('id'))
                if request.data[i].get('action') == 'delete':
                    availability.delete()
                else:
                    serializer = AvailabilitySerializer(availability, data=request.data[i])
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = AvailabilitySerializer(data=request.data[i])
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


class AvailabilitiesView(APIView):
    """List professional's availabilities"""
    permission_classes = [permissions.IsAuthenticated, AccessPermission]

    def get(self, request):
        if 'date' in request.GET:
            now = datetime. strptime(request.GET['date'].replace("T", " "), '%Y-%m-%d %H:%M:%S')
        else:
            now = timezone.now()
        initial_date = datetime.strftime(now, "%Y-%m-%d")
        final_date = dateformat.format(now + timedelta(days=7), 'Y-m-d')
        instance = User.objects.get(pk=request.GET['user_id'])
        data = []
        temp_weekday = ''

        if (instance.role == Constants.ROLE_PROFESSIONAL):

            availabilities = Availability.objects.filter(
                professional=instance.id, start_date__gte=initial_date,
                end_date__lte=final_date
            ).order_by('start_date')

            for aval in availabilities:

                temp_date = datetime.strftime(aval.start_date, "%Y-%m-%d")
                if aval.all_day is True or aval.appointment_duration == 0:

                    # No tiene agenda disponible
                    data.append({
                        'weekday': aval.weekday,
                        'all_day': aval.all_day,
                        'date': temp_date,
                        'duration': aval.appointment_duration,
                        'data': []
                    })

                else:

                    delta = timedelta(minutes=int(aval.appointment_duration))

                    if temp_weekday != aval.weekday:
                        temp_weekday = aval.weekday
                        temp_data = []
                        temp_available = []
                    else:
                        data = data[0:len(data)-1]

                    start_date = datetime.combine(
                        datetime.date(aval.start_date),
                        datetime.time(aval.start_date)
                    )
                    end_date = datetime.combine(
                        datetime.date(aval.end_date),
                        datetime.time(aval.end_date)
                    )

                    while start_date <= end_date:
                        temp_data.append(datetime.strftime(start_date, "%H:%M"))
                        appointment = Appointment.objects.filter(professional=instance, start_date__gte=start_date,
                                                                 end_date__lte=(start_date + delta)).first()
                        if appointment is None:
                            temp_available.append(True)
                        else:
                            temp_available.append(False)
                        # Add minutes to range date
                        start_date = start_date + delta

                    # Guardamos la información recogida
                    info = {
                        'weekday': temp_weekday,
                        'all_day': aval.all_day,
                        'date': temp_date,
                        'duration': aval.appointment_duration,
                        'data': temp_data,
                        'available': temp_available
                    }
                    data.append(info)

        return Response(data)


class ScheduleRecordsView(APIView):
    """Add service to the professional"""
    permission_classes = [permissions.IsAuthenticated, AccessPermission]

    def _getWeekDay(self, weekday):
        if (weekday == 7):
            return 0
        return weekday

    def _getDate(self, date, ref_date):
        new_date = date - timedelta(days=(date.isoweekday() % 7)) + \
            timedelta(days=self._getWeekDay(ref_date.isoweekday()))
        aux = datetime(year=ref_date.year, month=ref_date.month, day=ref_date.day)
        result = new_date - aux
        resp = ref_date + timedelta(days=result.days)
        return resp

    def _notAvailable(self, index, list, new_list, date):
        if not list[index].can_work:
            new_list.append({
                'availabilityId': list[index].id,
                'title': 'No disponible',
                'startDate': self._getDate(date, list[index].start_date),
                'endDate': self._getDate(date, list[index].end_date),
                'all_day': True,
                'groupId': 0,
                'attentionMethod': 4,
            })
        elif index == 0 and len(list) == 1:
            start_date = list[index].start_date
            end_date = list[index].end_date
            if not (start_date.hour == 6 and start_date.minute == 0):
                if((start_date.hour != 6 and start_date.minute != 0)
                        or (start_date.hour == 6 and start_date.minute != 0)
                        or (start_date.hour != 6 and start_date.minute == 0)):
                    start_date = datetime(start_date.year, start_date.month, start_date.day, 6)
                    end_date = list[index].start_date
                new_list.append({
                    'availabilityId': list[index].id,
                    'title': 'No disponible',
                    'startDate': self._getDate(date, start_date),
                    'endDate': self._getDate(date, end_date),
                    'all_day': False,
                    'groupId': 0,
                    'attentionMethod': 4,
                })
            start_date = list[index].end_date
            end_date = datetime(start_date.year, start_date.month, start_date.day, 23, 59)
            new_list.append({
                'availabilityId': list[index].id,
                'title': 'No disponible',
                'startDate': self._getDate(date, start_date),
                'endDate': self._getDate(date, end_date),
                'all_day': False,
                'groupId': 0,
                'attentionMethod': 4,
            })
        elif index == 0:
            start_date = list[index].start_date
            end_date = list[index].end_date
            if not (start_date.hour == 6 and start_date.minute == 0):
                if((start_date.hour != 6 and start_date.minute != 0)
                        or (start_date.hour == 6 and start_date.minute != 0)
                        or (start_date.hour != 6 and start_date.minute == 0)):
                    start_date = datetime(start_date.year, start_date.month, start_date.day, 6)
                    end_date = list[index].start_date
                new_list.append({
                    'availabilityId': list[index].id,
                    'title': 'No disponible',
                    'startDate': self._getDate(date, start_date),
                    'endDate': self._getDate(date, end_date),
                    'all_day': False,
                    'groupId': 0,
                    'attentionMethod': 4,
                })
        elif index == len(list) - 1:
            start_date = list[index - 1].end_date
            end_date = list[index].start_date
            new_list.append({
                'availabilityId': list[index].id,
                'title': 'No disponible',
                'startDate': self._getDate(date, start_date),
                'endDate': self._getDate(date, end_date),
                'all_day': False,
                'groupId': 0,
                'attentionMethod': 4,
            })
            start_date = list[index].end_date
            end_date = datetime(start_date.year, start_date.month, start_date.day, 23, 59)
            new_list.append({
                'availabilityId': list[index].id,
                'title': 'No disponible',
                'startDate': self._getDate(date, start_date),
                'endDate': self._getDate(date, end_date),
                'all_day': False,
                'groupId': 0,
                'attentionMethod': 4,
            })
        else:
            start_date = list[index - 1].end_date
            end_date = list[index].start_date
            new_list.append({
                'availabilityId': list[index].id,
                'title': 'No disponible',
                'startDate': self._getDate(date, start_date),
                'endDate': self._getDate(date, end_date),
                'all_day': False,
                'groupId': 0,
                'attentionMethod': 4,
            })

    def get(self, request):
        """Handle HTTP GET requ est."""
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        except Exception:
            return Response('Fechas no válida', status=status.HTTP_400_BAD_REQUEST)

        list = []
        for i in range(0, 7):
            availabilities = Availability.objects.filter(
                start_date__gte=start_date,
                end_date__lte=(end_date + timedelta(days=1)),
                professional=request.user,
                weekday_order=i
            ).order_by('weekday_order', 'start_date')
            for j in range(0, len(availabilities)):
                self._notAvailable(j, availabilities, list, start_date)
        appointments = Appointment.objects.filter(
            start_date__gte=start_date, end_date__lte=end_date, status=Constants.APPOINTMENT_PAID
        ) | Appointment.objects.filter(
            start_date__gte=start_date, end_date__lte=end_date, status=Constants.APPOINTMENT_CANCELED
        )
        for item in appointments:
            patient = ''
            if (item.patient):
                patient = '{} {}'.format(item.patient.first_name, item.patient.last_name)
            list.append({
                'appointmentId': item.id,
                'title': item.title,
                'patient': patient,
                'startDate': item.start_date,
                'endDate': item.end_date,
                'alDay': False,
                'groupId': 0,
                'status': item.status,
                'duration': item.appointment_duration,
            })
        return Response(list)

    def patch(self, request):
        """Handle HTTP PATCH request."""
        try:
            appointment = Appointment.objects.get(pk=request.data.get('pk'))
            serializer = AppointmentSerializer(
                appointment,
                data=request.data.get('data'),
                partial=True
            )
            if(serializer.is_valid()):
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Appointment.DoesNotExist:
            return Response('Cita no encontrada', status=status.HTTP_400_BAD_REQUEST)


class RescheduleDetailView(APIView):
    """Add service to the professional"""
    permission_classes = [permissions.IsAuthenticated, AccessPermission]

    def put(self, request):
        """Handle HTTP PUT request."""
        try:
            appointment = Appointment.objects.get(pk=request.data.get('appointmentId'))
            appointment.appointment_duration = int(request.data.get('duration', appointment.appointment_duration))
            appointment.start_date = datetime.strptime(request.data.get('startDate'), '%Y-%m-%d %H:%M')
            appointment.end_date = appointment.start_date + \
                timedelta(minutes=int(request.data.get('duration', appointment.appointment_duration)))
            appointment.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # except Service.DoesNotExist:
        #     return Response({'msg': 'Servicio no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
        except Appointment.DoesNotExist:
            return Response({'msg': 'Cita no encontrada'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            return Response({'msg': 'El valor de la duración debe ser un número entero'}, status=status.HTTP_400_BAD_REQUEST)


class ReportPatientAppointmentView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        kws = {
            'request_datetime__gte': request.GET['date_init'],
            'request_datetime__lte': request.GET['date_end']
        }
        list = PatientAppointment.objects.filter(**kws)
        serializer = FullPatientAppointmentSerializer(list, many=True)
        return Response(serializer.data)


class PatientAppointmentView(APIView):
    """Add service to the professional"""
    permission_classes = [permissions.IsAuthenticated, AccessPermission]

    def post(self, request):
        """Handle HTTP POST request."""
        start_date = datetime.strptime(request.data['start_date'].replace("T", " "), '%Y-%m-%d %H:%M:%S')
        end_date = start_date + timedelta(minutes=int(request.data['appointment_duration']))
        appointment_serializer = AppointmentSerializer(data={
            'patient': request.data['patient']['id'],
            'professional': request.data['professionals'],
            'start_date': request.data['start_date'],
            'end_date': end_date,
            'status': Constants.APPOINTMENT_PAID,
            'appointment_duration': request.data['appointment_duration'],
            'title': 'Cita programada, paciente: {} {}'.format(request.data['patient']['firstName'], request.data['patient']['surname']),
            'description': request.data['observations']
        })
        if(appointment_serializer.is_valid()):
            appointment_serializer.save()
            patient_appointment_serializer = PatientAppointmentSerializer(data={
                'user': request.data['user']['id'],
                'appointment': appointment_serializer.data['id'],
                'state': request.data['states'],
                'type_request': request.data['request_type'],
                'request_datetime': request.data['request_datetime'],
                'suggested_datetime': request.data['suggested_datetime'],
                'patient_appointment_uuid': request.data['appointment_id'],
                'ips': request.data['ips'],
                'production_code': request.data['production_center'],
                'sale_document': request.data['sale_document'],
                'first_time': request.data['first_time'],
                'programs': request.data['programs']
            })
            if(patient_appointment_serializer.is_valid()):
                patient_appointment_serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(patient_appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentPurposeView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        appointmentPurposes = AppointmentPurpose.objects.all()
        serializer = AppointmentPurposeSerializer(appointmentPurposes, many=True)
        return Response(serializer.data)
