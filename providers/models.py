from __future__ import unicode_literals
from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Provider(models.Model):
    name = models.CharField(max_length=65)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = PhoneNumberField(unique=True)
    language = models.CharField(max_length=20)
    currency = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class ProviderPolygon(models.Model):
    provider = models.OneToOneField(Provider)
    polygon_name = models.CharField(max_length=40)
    price = models.PositiveSmallIntegerField()
    poly = models.PolygonField()

    objects = models.GeoManager()

    def __unicode__(self):
        return self.polygon_name
