from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from . import serializers, models

# Create your views here.


class TaskTypeView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Task_type.objects.all()
    serializer_class = serializers.TaskTypeSerializer


class TaskView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class TaskRecordView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Task_record.objects.all()
    serializer_class = serializers.TaskRecordSerializer
