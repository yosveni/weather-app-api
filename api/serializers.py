from rest_framework import serializers, fields
from rest_framework.authtoken.models import Token
from .models import Weather
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class WeatherSerializer(serializers.ModelSerializer):
    request_date = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])

    class Meta:
        model = Weather
        fields = ('id', 'user', 'request_date', 'data')
