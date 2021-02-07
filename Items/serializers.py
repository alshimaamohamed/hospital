from rest_framework import serializers
from . import models


class AnchorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Anchor
        fields = '__all__'


class EdgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Edge
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Meal
        fields = '__all__'


class FoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Food_item
        fields = '__all__'


class MedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Medicine
        fields = '__all__'



class RobotSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Robot
        fields = '__all__'
