from django.apps import AppConfig


class PanelProviderPricingConfig(AppConfig):
  name = "panel_provider_pricing"
  verbose_name = "Panel Provider Pricing"

  def ready(self):
    import panel_provider_pricing.models
