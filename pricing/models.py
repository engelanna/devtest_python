from django.db import models
from encrypted_model_fields.fields import EncryptedCharField


class PanelProvider(models.Model):
  def __str__(self): return "code: %s" % self.code

  code = models.CharField(max_length=20)


class TargetGroup(models.Model):
  def __str__(self): return "%s, external_id: %s" % (self.name, self.external_id)

  parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
  panel_provider = models.ForeignKey(PanelProvider, null=True, on_delete=models.SET_NULL)

  external_id = models.IntegerField(default=None)
  name = models.CharField(max_length=100)
  secret_code = EncryptedCharField(max_length=100)


class Country(models.Model):
  def __str__(self): return "country_code: %s" % self.country_code

  panel_provider = models.ForeignKey(PanelProvider, null=True, on_delete=models.SET_NULL)
  target_groups = models.ManyToManyField(TargetGroup) # TODO: Only root nodes

  country_code = models.CharField(max_length=20)


class LocationGroup(models.Model):
  def __str__(self): return "name: %s" % self.name

  country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
  panel_provider = models.ForeignKey(PanelProvider, null=True, on_delete=models.SET_NULL)

  name = models.CharField(max_length=100)


class Location(models.Model):
  def __str__(self): return "name: %s" % self.name

  location_groups = models.ManyToManyField(LocationGroup)

  external_id = models.IntegerField(default=None)
  name = models.CharField(max_length=100)
  secret_code = EncryptedCharField(max_length=100)




"""
3 Countries, each with different panel provider
3 Panel Providers
20 Locations of any type (city, region, state, etc.)
4 Location Groups, 3 of them with different provider and 1 would belong to any of them
4 root Target Groups and each root should start a tree which is minimium 3 levels deep (3 of them with different provider and 1 would belong to any of them)
"""
