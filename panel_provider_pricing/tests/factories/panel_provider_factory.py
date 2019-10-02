from faker import Faker

from .models import PanelProvider as DefaultModel


class PanelProviderFactory():

    @staticmethod
    def create(panel_provider_model=DefaultModel):
        new_provider = build(panel_provider_model)
        new_provider.save()

        return new_provider

    @staticmethod
    def build(panel_provider_model=DefaultModel):
        new_provider = panel_provider_model()
        new_provider.code = Faker().bs()

        return new_provider
