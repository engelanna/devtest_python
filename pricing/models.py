from django.db import models
from encrypted_model_fields.fields import EncryptedCharField
from lxml import html
import requests


class PanelProvider(models.Model):
    code = models.CharField(max_length=20)

    class Meta:
        db_table = "panel_providers"

    def __repr__(self):
        return F"{self.id}, code: {self.code}"


class TargetGroup(models.Model):
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    panel_provider = models.ForeignKey(PanelProvider, null=True, on_delete=models.SET_NULL)

    external_id = models.IntegerField(default=None)
    name = models.CharField(max_length=100)
    secret_code = EncryptedCharField(max_length=100)

    class Meta:
        db_table = "target_groups"

    def __repr__(self):
        return F"{self.id}, name: {self.name}, external_id: {self.external_id}"


class Country(models.Model):
    panel_provider = models.ForeignKey(PanelProvider, null=True, on_delete=models.SET_NULL)
    target_groups = models.ManyToManyField(TargetGroup)

    country_code = models.CharField(max_length=20)

    class Meta:
        db_table = "countries"

    def __repr__(self):
        return F"{self.id}, country_code: {self.country_code}"


class LocationGroup(models.Model):
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    panel_provider = models.ForeignKey(PanelProvider, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=100)

    class Meta:
        db_table = "location_groups"

    def __repr__(self):
        return F"{self.id}, name: {self.name}"


class Location(models.Model):
    location_groups = models.ManyToManyField(LocationGroup)

    panel_size = models.IntegerField(default=0)
    external_id = models.IntegerField(default=None)
    name = models.CharField(max_length=100)
    secret_code = EncryptedCharField(max_length=100)

    class Meta:
        db_table = "locations"

    def __repr__(self):
        return F"{self.id}, name: {self.name}, panel_size: {self.panel_size}"

