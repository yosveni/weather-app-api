import datetime
import json
from django.contrib.auth.models import User
from django.test import TestCase, Client
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .serializers import *

# Create your tests here.


client = APIClient()

class WeatherViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User(
            username='test',
            password='test123'
        )
        self.user.save()

    def test_add_weather(self):

        data = {
            'user': self.user.id,
            'request_date': datetime.datetime.now(),
            'data': {
                'city_id': 3440648,
                'temperature':  20.56,
                'humidity': 93
            }
        }
        response = client.post(
            '/api/weather/1/add_weather/',
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)




