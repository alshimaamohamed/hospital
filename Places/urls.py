from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('HospitalAPI', views.HospitalView)
router.register('BuildingAPI', views.BuildingView)
router.register('FloorAPI', views.FloorView)
router.register('PharmacyAPI', views.PharmacyView)
router.register('KitchenAPI', views.KitchenView)
router.register('RoomAPI', views.RoomView)
router.register('ScanlabAPI', views.ScanlabView)
router.register('OfficeAPI', views.OfficeView)
router.register('DepartmentAPI', views.DepartmentView)
router.register('ChargingStationAPI', views.ChargingStationView)
router.register('BiolabsAPI', views.BiolabsView)
router.register('ReceptionAPI', views.ReceptionView)

urlpatterns = [
    path('', include(router.urls))
]
