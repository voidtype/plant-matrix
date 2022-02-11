# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken import views as authviews

router = routers.DefaultRouter()
router.register(r'configs', views.DeviceConfigViewSet)
router.register(r'readings', views.SensorReadingViewSet)
router.register(r'samples', views.SampleViewSet)
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]