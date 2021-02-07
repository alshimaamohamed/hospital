from rest_framework import serializers
from . import models


class TaskTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task_type
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = '__all__'


class TaskRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task_record
        fields = '__all__'
