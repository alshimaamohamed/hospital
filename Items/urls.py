from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('AnchorAPI', views.AnchorView)
router.register('EdgeAPI', views.EdgeView)
router.register('MealAPI', views.MealView)
router.register('FoodItemAPI', views.FoodItemView)
router.register('MedicineAPI', views.MedicineView)
router.register('RobotAPI', views.RobotView)


urlpatterns = [
    path('', include(router.urls))
]
