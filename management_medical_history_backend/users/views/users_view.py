"""Users views."""

# Django
from management_medical_history_backend.users.serializers.user_serializer import UserSerializer
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Django REST Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from management_medical_history_backend.users.models import (
    User, Token, Profile,
)

# Utilities
from management_medical_history_backend.utils import Constants
from datetime import datetime, timedelta
import uuid
import environ


class ResetPasswordView(APIView):
    """View for reset password"""

    def _sendEmail(self, subject, from_email, to_email, params, email_html_message, email_plaintext_message):
        """Send email"""
        env = environ.Env()

        # render email text
        email_html_message = render_to_string('email/user_reset_password.html', params)
        email_plaintext_message = render_to_string('email/user_reset_password.txt', params)

        msg = EmailMultiAlternatives(
            # title:
            subject,
            # message:
            email_plaintext_message,
            # from:
            from_email,
            # to:
            to_email
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""
        try:
            user = User.objects.get(
                email=request.data.get('email')
            )
        except User.DoesNotExist:
            return Response({'msg': 'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'msg': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            env = environ.Env()
            now = datetime.now()
            token = Token.objects.create(
                user=user,
                type=Constants.TYPE_RESET_PASSWORD,
                key=str(uuid.uuid4()),
                valid_until=(now + timedelta(minutes=env.int('DJANGO_TOKEN_DURATION', 10))),
            )

            self._sendEmail(
                subject='Password Reset for Siellano',
                from_email='edwin.javier.castano@gmail.com',
                to_email=[user.email],
                email_html_message='email/user_reset_password.html',
                email_plaintext_message='email/user_reset_password.txt',
                params={
                    'reset_password_url': "{}/{}/{}".format(
                        env('SIELLANO_WEB_URL'),
                        'reset-password-confirm',
                        token.key
                    )
                },
            )

            return Response({'msg': 'ok'})
        except Exception as ex:
            return Response({'msg': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ConfirmTokenView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            token = Token.objects.get(
                key=request.data.get('token'),
                is_available=True,
            )
        except Token.DoesNotExist:
            return Response({'msg': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'msg': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        user = User.objects.get(id=token.user.id)
        if token.type == Constants.TYPE_ACCOUNT_CONFIRMATION:
            user.is_verified = True
            token.is_available = False
            user.save()
            token.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        now = datetime.now()
        if token.valid_from <= now and token.valid_until >= now:
            if token.type == Constants.TYPE_RESET_PASSWORD:
                try:
                    password_validation.validate_password(request.data.get('password'))
                    token.is_available = False
                    user.password = make_password(request.data.get('password'))
                    token.save()
                    user.save()
                    return Response({'msg': 'ok'})
                except ValidationError as ex:
                    return Response({'password': ' '.join(str(e) for e in ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                except Exception as ex:
                    return Response({'msg': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'msg': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        if 'role' in request.GET:
            user = User.objects.filter(role=request.GET['role'])
        else:
            user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


class IndexCardHolderView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        try:
            profile = Profile.objects.get(nuip=request.query_params.get('nuip'))
            serializer = UserSerializer(profile.user)
            return Response(serializer.data)
        except Profile.DoesNotExist as ex:
            return Response({'msg': 'Paciente no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """Handle HTTP PUT request."""
        try:
            user = User.objects.get(email=request.data.get('email'))
            if (request.data.get('email') is None or request.data.get('nuip') is None):
                return Response(
                    {'msg': 'El email y número de identificación son obligatorios'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            email = request.data.get('email')
            first_name = request.data.get('first_name')
            second_name = request.data.get('second_name')
            surname = request.data.get('surname')
            second_surname = request.data.get('second_surname')
            data = {
                'email': email,
                'first_name': first_name,
                'second_name': second_name,
                'surname': surname,
                'second_surname': second_surname,
                'profile': request.data,
            }
            serializer = UserSerializer(user, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            if (request.data.get('email') is None or request.data.get('nuip') is None):
                return Response(
                    {'msg': 'El email y número de identificación son obligatorios'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            username = request.data.get('email')
            email = request.data.get('email')
            first_name = request.data.get('first_name')
            second_name = request.data.get('second_name')
            surname = request.data.get('surname')
            second_surname = request.data.get('second_surname')
            data = {
                'username': username,
                'email': email,
                'first_name': first_name,
                'second_name': second_name,
                'surname': surname,
                'second_surname': second_surname,
                'role': Constants.ROLE_PATIENT,
                'password': email,
                'profile': request.data,
            }
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'msg': str(ex)}, status=status.HTTP_400_BAD_REQUEST)
