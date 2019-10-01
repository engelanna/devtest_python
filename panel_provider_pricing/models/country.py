from django.db import models
from panel_provider_pricing.models import PanelProvider, TargetGroup

class Country(models.Model):
    panel_provider = models.ForeignKey(PanelProvider, null=True, on_delete=models.SET_NULL)
    target_groups = models.ManyToManyField(TargetGroup)

    country_code = models.CharField(max_length=20)

    class Meta:
        db_table = "countries"

    def __repr__(self):
        return F"{self.id}, country_code: {self.country_code}"
