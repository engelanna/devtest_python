from faker import Faker

from panel_provider_pricing.models import PanelProvider


class PanelProviderFactory():

    @classmethod
    def create(cls):
        new_provider = cls.build()
        new_provider.save()

        return new_provider

    @classmethod
    def build(cls):
        new_provider = PanelProvider()
        new_provider.code = Faker().bs()

        return new_provider
