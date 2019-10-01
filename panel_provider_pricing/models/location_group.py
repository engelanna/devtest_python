from django.db import models

from .country import Country
from .panel_provider import PanelProvider


class LocationGroup(models.Model):
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    panel_provider = models.ForeignKey(PanelProvider, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=100)

    class Meta:
        db_table = "location_groups"

    def __repr__(self):
        return F"{self.id}, name: {self.name}"

