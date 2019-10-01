from django.db import models
from django.dispatch import receiver
from models.signals import m2m_changed

from panel_provider_pricing.models import PanelProvider, TargetGroup


class Country(models.Model):
    panel_provider = models.ForeignKey(PanelProvider, null=True, on_delete=models.SET_NULL)
    target_groups = models.ManyToManyField(TargetGroup)

    country_code = models.CharField(max_length=20)

    class Meta:
        db_table = "countries"

    def __repr__(self):
        return F"{self.id}, country_code: {self.country_code}"


@receiver(m2m_changed, sender=Country.target_groups.through)
def check_if_all_target_groups_root(sender, **kwargs):
    for pk in kwargs["pk_set"]:
        target_group = kwargs["model"].objects.get(pk=pk)

        if target_group.parent is not None:
            raise ValueError("All target groups for a country must be root")
