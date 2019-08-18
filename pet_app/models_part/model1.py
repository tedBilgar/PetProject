from django.db import models


class Weather(models.Model):
    name = models.CharField(max_length=50, null=False)
    active = models.BooleanField()
