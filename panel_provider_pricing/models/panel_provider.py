from django.db import models


class PanelProvider(models.Model):
    code = models.CharField(max_length=255)
    price_calculation_strategy = models.CharField(max_length=255,
        default="CharacterCount")


    class Meta:
        db_table = "panel_providers"

    def __repr__(self):
        return f"{self.id}, code: {self.code}"
