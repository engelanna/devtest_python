from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

from .location_group import LocationGroup


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

