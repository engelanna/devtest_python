from django.db import models


class PanelProvider(models.Model):
    code = models.CharField(max_length=20)

    class Meta:
        db_table = "panel_providers"

    def __repr__(self):
        return F"{self.id}, code: {self.code}"
