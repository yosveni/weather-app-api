from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db.models import JSONField


class Weather(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    request_date = models.DateTimeField()
    data = JSONField()

