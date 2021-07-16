"""Users URLs"""

# Django
from django.urls import path

# Django REST framework
from rest_framework.urlpatterns import format_suffix_patterns

# Views
from management_medical_history_backend.services.views import (
    NacionalityView,
    CountryView,
    DepartmentView,
    DiagnoseView,
    CategoryView,
    CityView,
    UsualOccupationView,
    SpecialPopulationView,
    SexualOrientationView,
    SocialSecuritySchemeView,
    EpsView,
    CivilStatusView,
    ScholarshipView,
    EthnicGroupView,
    TypeDegreeDisabilityView,
    RelationshipPersonInChargeView,
    HcOpenPlaceView,
    HcTransferToView,
    TypeRequestView,
    StateView,
    ProgramView,
    ProductionCenterView,
    IpsView
)


urlpatterns = [
    path('api/nacionalities/', NacionalityView.as_view(), name='nacionalities'),
    path('api/countries/', CountryView.as_view(), name='countries'),
    path('api/diagnoses/', DiagnoseView.as_view(), name='diagnoses'),
    path('api/categories/', CategoryView.as_view(), name='categories'),
    path('api/deparments/<int:country_id>', DepartmentView.as_view(), name='deparments'),
    path('api/cities/<int:department_id>', CityView.as_view(), name='cities'),
    path('api/usual-occupation/', UsualOccupationView.as_view(), name='usual_occupation'),
    path('api/special-population/', SpecialPopulationView.as_view(), name='special_population'),
    path('api/sexual-orientation/', SexualOrientationView.as_view(), name='sexual_orientation'),
    path('api/social-security-scheme/', SocialSecuritySchemeView.as_view(), name='social_security_scheme'),
    path('api/eps/', EpsView.as_view(), name='eps'),
    path('api/civil-status/', CivilStatusView.as_view(), name='civil_status'),
    path('api/scholarship/', ScholarshipView.as_view(), name='scholarship'),
    path('api/ethnic-group/', EthnicGroupView.as_view(), name='ethnic-group'),
    path('api/type-degree-disability/', TypeDegreeDisabilityView.as_view(), name='type_degree_disability'),
    path('api/type-request/', TypeRequestView.as_view(), name='type_request'),
    path('api/state/', StateView.as_view(), name='state'),
    path('api/program/', ProgramView.as_view(), name='program'),
    path('api/production-center/', ProductionCenterView.as_view(), name='production_center'),
    path('api/ips/', IpsView.as_view(), name='ips'),
    path('api/relationship-person-in-charge/', RelationshipPersonInChargeView.as_view(), name='relationship_person_in_charge'),
    path('api/hc-open-place/', HcOpenPlaceView.as_view(), name='hc_open_place'),
    path('api/hc-transfer-to/', RelationshipPersonInChargeView.as_view(), name='hc_transfer_to'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
