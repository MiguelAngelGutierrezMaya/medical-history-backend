"""Users views."""

# Django REST Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from management_medical_history_backend.services.models import (
    Nacionality,
    Country,
    Department,
    Diagnose,
    Category,
    City,
    UsualOccupation,
    SpecialPopulation,
    SexualOrientation,
    SocialSecurityScheme,
    Eps,
    CivilStatus,
    Scholarship,
    EthnicGroup,
    TypeDegreeDisability,
    RelationshipPersonInCharge,
    HcOpenPlace,
    HcTransferTo,
)

# Serializers
from management_medical_history_backend.services.serializers import (
    NacionalitySerializer,
    CountrySerializer,
    DepartmentSerializer,
    DiagnoseSerializer,
    CategorySerializer,
    CitySerializer,
    UsualOccupationSerializer,
    SpecialPopulationSerializer,
    SexualOrientationSerializer,
    SocialSecuritySchemeSerializer,
    EpsSerializer,
    CivilStatusSerializer,
    ScholarshipSerializer,
    EthnicGroupSerializer,
    TypeDegreeDisabilitySerializer,
    RelationshipPersonInChargeSerializer,
    HcOpenPlaceSerializer,
    HcTransferToSerializer,
)


class NacionalityView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        nacionalities = Nacionality.objects.all()
        serializer = NacionalitySerializer(nacionalities, many=True)
        return Response(serializer.data)


class CountryView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)


class DepartmentView(APIView):
    def get(self, request, country_id):
        """Handle HTTP GET request."""
        deparments = Department.objects.filter(country__id=country_id)
        serializer = DepartmentSerializer(deparments, many=True)
        return Response(serializer.data)


class CityView(APIView):
    def get(self, request, department_id):
        """Handle HTTP GET request."""
        cities = City.objects.filter(department__id=department_id)
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


class DiagnoseView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        diagnoses = Diagnose.objects.all()
        serializer = DiagnoseSerializer(diagnoses, many=True)
        return Response(serializer.data)


class CategoryView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class UsualOccupationView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        usual_occupations = UsualOccupation.objects.all()
        serializer = UsualOccupationSerializer(usual_occupations, many=True)
        return Response(serializer.data)


class SpecialPopulationView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        special_populations = SpecialPopulation.objects.all()
        serializer = SpecialPopulationSerializer(special_populations, many=True)
        return Response(serializer.data)


class SexualOrientationView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        sexual_orientations = SexualOrientation.objects.all()
        serializer = SexualOrientationSerializer(sexual_orientations, many=True)
        return Response(serializer.data)
        return Response(serializer.data)


class SocialSecuritySchemeView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        social_security_schemes = SocialSecurityScheme.objects.all()
        serializer = SocialSecuritySchemeSerializer(social_security_schemes, many=True)
        return Response(serializer.data)


class EpsView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        eps = Eps.objects.all()
        serializer = EpsSerializer(eps, many=True)
        return Response(serializer.data)


class CivilStatusView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        civil_status = CivilStatus.objects.all()
        serializer = CivilStatusSerializer(civil_status, many=True)
        return Response(serializer.data)


class ScholarshipView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        scholarship = Scholarship.objects.all()
        serializer = ScholarshipSerializer(scholarship, many=True)
        return Response(serializer.data)


class EthnicGroupView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        ethnic_group = EthnicGroup.objects.all()
        serializer = EthnicGroupSerializer(ethnic_group, many=True)
        return Response(serializer.data)


class TypeDegreeDisabilityView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        type_degree_disability = TypeDegreeDisability.objects.all()
        serializer = TypeDegreeDisabilitySerializer(type_degree_disability, many=True)
        return Response(serializer.data)


class RelationshipPersonInChargeView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        relationship_person_in_charge = RelationshipPersonInCharge.objects.all()
        serializer = RelationshipPersonInChargeSerializer(relationship_person_in_charge, many=True)
        return Response(serializer.data)


class HcOpenPlaceView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        hc_open_place = HcOpenPlace.objects.all()
        serializer = HcOpenPlaceSerializer(hc_open_place, many=True)
        return Response(serializer.data)


class HcTransferToView(APIView):
    def get(self, request):
        """Handle HTTP GET request."""
        hc_transfer_to = HcTransferTo.objects.all()
        serializer = HcTransferToSerializer(hc_transfer_to, many=True)
        return Response(serializer.data)
