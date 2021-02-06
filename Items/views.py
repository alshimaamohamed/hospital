from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from . import serializers, models

# Create your views here.


class AnchorView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Anchor.objects.all()
    serializer_class = serializers.AnchorSerializer


class EdgeView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Edge.objects.all()
    serializer_class = serializers.EdgeSerializer


class MealView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Meal.objects.all()
    serializer_class = serializers.MealSerializer


class FoodItemView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Food_item.objects.all()
    serializer_class = serializers.FoodItemSerializer


class MedicineView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.Medicine.objects.all()
    serializer_class = serializers.MedicineSerializer
