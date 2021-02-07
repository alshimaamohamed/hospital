from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('PersonAPI', views.PersonView)
router.register('DoctorAPI', views.DoctorView)
router.register('NurseAPI', views.NurseView)
router.register('ReceptionistAPI', views.ReceptionistView)
router.register('PatientAPI', views.PatientView)
router.register('HospitalManagerAPI', views.HospitalManagerView)
router.register('DepartmentManagerAPI', views.DepartmentManagerView)
router.register('PatientMateAPI', views.PatientMateView)
router.register('MeasurementsAPI', views.MeasurementsView)

urlpatterns = [
    path('', include(router.urls))
]
