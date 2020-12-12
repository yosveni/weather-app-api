from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, WeatherViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('weather', WeatherViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('get_data/', get_data, name='get_data')
]
