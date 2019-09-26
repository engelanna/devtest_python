from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from pricing.models import Country

@receiver(m2m_changed, sender=Country.target_groups.through)
def are_all_target_groups_root(sender, **kwargs):
  for pk in kwargs["pk_set"]:
    if kwargs["model"].objects.get(pk=pk).parent != None:
      raise ValueError("All target groups for a country must be root")
