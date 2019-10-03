from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .panel_provider import PanelProvider
from .target_group import TargetGroup


class Country(models.Model):
    panel_provider = models.ForeignKey(PanelProvider, null=True, on_delete=models.SET_NULL)
    target_groups = models.ManyToManyField(TargetGroup)

    country_code = models.CharField(max_length=255)

    class Meta:
        db_table = "countries"

    def __repr__(self):
        return f"{self.id}, country_code: {self.country_code}"


@receiver(m2m_changed, sender=Country.target_groups.through)
def check_if_all_target_groups_root(sender, **kwargs):
    """
    Called whenever the many-to-many relationship with target groups changes
    """

    for pk in kwargs["pk_set"]:
        target_group = kwargs["model"].objects.get(pk=pk)

        if target_group.parent is not None:
            raise ValueError("All target groups for a country must be root")
