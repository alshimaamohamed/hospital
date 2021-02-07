from rest_framework import permissions
from drf_yasg import openapi
from django.conf.urls import url
from django.urls import reverse
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view





schema_view = get_schema_view(
   openapi.Info(
      title="Hospital API",
      default_version='v1',
      description="Hospital api for robot navigation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="nabilmokhtar15@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
    path('Items/', include('Items.urls')),
    path('Person/', include('Person.urls')),
    path('Places/', include('Places.urls')),
    path('Tasks/', include('Tasks.urls')),
   # path(, include('rest_framework_docs.urls')),
    url('docs/', schema_view),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),



]

