from rest_framework import serializers
from . import models


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = '__all__'

class PatientMateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Patient_Mate
        fields = '__all__'

class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Mesurements
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Doctor
        fields = '__all__'


class NurseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Nurse
        fields = '__all__'


class ReceptionistSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Receptionist
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Patient
        fields = '__all__'


class HospitalManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Hospital_manager
        fields = '__all__'


class DepartmentManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Department_manager
        fields = '__all__'


