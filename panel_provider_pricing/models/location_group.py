from django.db import models

from panel_provider_pricing.models import Country, PanelProvider


class LocationGroup(models.Model):
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    panel_provider = models.ForeignKey(PanelProvider, null=True, on_delete=models.SET_NULL)

    name = mdels.CharField(max_length=100)

    class Meta:
        db_table = "location_groups"

    def __repr__(self):
        return F"{self.id}, name: {self.name}"

