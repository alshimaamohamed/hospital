from rest_framework import serializers
from . import models


class HospitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Hospital
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Building
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Floor
        fields = '__all__'


class PharmacySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pharmacy
        fields = '__all__'


class KitchenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Kitchen
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Room
        fields = '__all__'


class ScanlabSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Scan_lab
        fields = '__all__'


class OfficeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Office
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Department
        fields = '__all__'


class ChargingStationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Charging_station
        fields = '__all__'


class BiolabsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Bio_labs
        fields = '__all__'


class ReceptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Reception
        fields = '__all__'
