from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

from .panel_provider import PanelProvider


class TargetGroup(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    panel_provider = models.ForeignKey(PanelProvider, null=True, on_delete=models.SET_NULL)

    external_id = models.IntegerField(default=None)
    name = models.CharField(max_length=100)
    secret_code = EncryptedCharField(max_length=100)

    class Meta:
        db_table = "target_groups"

    def __repr__(self):
        return F"{self.id}, name: {self.name}, external_id: {self.external_id}"
