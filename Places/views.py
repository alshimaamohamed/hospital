from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from . import serializers, models

# Create your views here.


class HospitalView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Hospital.objects.all()
    serializer_class = serializers.HospitalSerializer


class BuildingView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingSerializer


class FloorView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Floor.objects.all()
    serializer_class = serializers.FloorSerializer


class PharmacyView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Pharmacy.objects.all()
    serializer_class = serializers.PharmacySerializer


class KitchenView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Kitchen.objects.all()
    serializer_class = serializers.KitchenSerializer


class RoomView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class ScanlabView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Scan_lab.objects.all()
    serializer_class = serializers.ScanlabSerializer


class OfficeView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Office.objects.all()
    serializer_class = serializers.OfficeSerializer


class DepartmentView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class ChargingStationView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Charging_station.objects.all()
    serializer_class = serializers.ChargingStationSerializer


class BiolabsView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Bio_labs.objects.all()
    serializer_class = serializers.BiolabsSerializer


class ReceptionView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Reception.objects.all()
    serializer_class = serializers.ReceptionSerializer
