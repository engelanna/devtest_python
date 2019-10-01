from django.apps import AppConfig

class PanelProviderPricingConfig(AppConfig):
  name = 'panel_provider_pricing'

  def ready(self):
    import panel_provider_pricing.signals
