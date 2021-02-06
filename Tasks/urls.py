from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('TaskTypeAPI', views.TaskTypeView)
router.register('TaskAPI', views.TaskView)
router.register('TaskRecordAPI', views.TaskRecordView)

urlpatterns = [
    path('', include(router.urls))
]
