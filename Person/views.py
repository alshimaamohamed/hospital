from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from . import serializers, models

# Create your views here.


class PersonView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class DoctorView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer


class NurseView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Nurse.objects.all()
    serializer_class = serializers.NurseSerializer


class ReceptionistView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Receptionist.objects.all()
    serializer_class = serializers.ReceptionistSerializer


class PatientView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer


class HospitalManagerView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Hospital_manager.objects.all()
    serializer_class = serializers.HospitalManagerSerializer


class DepartmentManagerView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Department_manager.objects.all()
    serializer_class = serializers.DepartmentManagerSerializer
