from django.db import models
from django_google_maps import fields as map_fields


class Shop(models.Model):
    name = models.CharField(max_length=225)
    logo = models.ImageField(default='default.png')
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

    def __str__(self):
        return f"{self.name}"
