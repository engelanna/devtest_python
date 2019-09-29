from django.db import models
from encrypted_model_fields.fields import EncryptedCharField
from lxml import html
import requests


class PanelProvider(models.Model):
    code = models.CharField(max_length=20)

    def __repr__(self): return "%s, code: %s" % (self.id, self.code)


class TargetGroup(models.Model):
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    panel_provider = models.ForeignKey(PanelProvider, null=True, on_delete=models.SET_NULL)

    external_id = models.IntegerField(default=None)
    name = models.CharField(max_length=100)
    secret_code = EncryptedCharField(max_length=100)

    def __repr__(self):
        return "%s, name: %s, external_id: %s" % (self.id, self.name, self.external_id)


class Country(models.Model):
    panel_provider = models.ForeignKey(PanelProvider, null=True, on_delete=models.SET_NULL)
    target_groups = models.ManyToManyField(TargetGroup)

    country_code = models.CharField(max_length=20)

    def __repr__(self):
        return "%s, country_code: %s" % (self.id, self.country_code)


class LocationGroup(models.Model):
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    panel_provider = models.ForeignKey(PanelProvider, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=100)

    def __repr__(self): return "%s, name: %s" % (self.id, self.name)


class Location(models.Model):
    location_groups = models.ManyToManyField(LocationGroup)

    external_id = models.IntegerField(default=None)
    name = models.CharField(max_length=100)
    secret_code = EncryptedCharField(max_length=100)

    def __repr__(self): return "%s, name: %s" % (self.id, self.name)

