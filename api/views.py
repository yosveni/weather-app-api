import datetime
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, WeatherSerializer
from django.contrib.auth.models import User
from .models import Weather
from .helpers import *


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    # authentication_classes = (Tok)

    @action(detail=True, methods=['POST'])
    def add_weather(self, request, pk=None):
        request_date = datetime.datetime.now()
        cities = get_cities()
        response = asyncio.run(fetch_all(cities))
        data = [
            {'city_id': res['id'],
             'temperature': res['main']['temp_max'],
             'humidity': res['main']['humidity']}
            for res in response]

        try:
            user = User.objects.get(id=pk)
            weather = Weather(
                user=user,
                request_date=request_date,
                data=data
            )
            weather.save()
            serializer = WeatherSerializer(weather, many=False)
            response = {'message': 'Weather saved!!', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        except:
            response = {'message': 'You need to provide weather data'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def get_data(self, request):
        response = {'message': 'Ayncio Example'}
        return Response(response, status=status.HTTP_200_OK)
