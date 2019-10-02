from django.db import transaction

from .seeders import PanelProviderSeeder, TargetGroupSeeder, CountrySeeder, LocationGroupSeeder, LocationSeeder

class SeedTheDatabase():
    """
    Provides initial data for a fresh install to work with.
    """

    @classmethod
    def execute(cls, apps_registry, _schema_editor):
        with transaction.atomic():
          panel_providers = cls._seed_panel_providers(apps_registry)
          cls._seed_target_groups(apps_registry, panel_providers)


        create_target_groups(get_model("TargetGroup"), panel_provider_ids)

        # country_ids = create_countries(get_model("Country"), panel_provider_ids)

        # create_location_groups(get_model("LocationGroup"),
        #   panel_provider_ids, country_ids)
        # create_locations(get_model("Location"))


    @classmethod
    def _seed_panel_providers(cls, apps_registry):
        model_class = apps_registry.get_model(
            "panel_provider_pricing", "PanelProvider")
        panel_providers = []

        for _ in range(3):
            panel_providers.append(PanelProviderFactory(model_class))

    @classmethod
    def _seed_target_groups(cls, apps_registry, panel_providers):
        model = apps_registry.get_model(
            "panel_provider_pricing", "TargetGroup")

        panel_providers = []

                for _ in range(4):
            pass






def create_countries(Country, all_provider_choices):
    remaining_providers = set(all_provider_choices)
    newly_inserted_ids = []
    faker = Faker()

    for _ in range(3):
        new_country = Country()
        new_country.country_code = faker.country_code()
        new_country.panel_provider_id = \
          remaining_providers.pop() if any(remaining_providers) else random.choice(all_provider_choices)
        new_country.save()
        newly_inserted_ids.append(new_country.id)

    return newly_inserted_ids


def create_location_groups(LocationGroup, all_provider_choices, country_ids):
    remaining_providers = set(all_provider_choices)
    faker = Faker()

    for _ in range(4):
        new_group = LocationGroup()
        new_group.country_id = random.choice(country_ids)
        new_group.name = faker.country()
        new_group.panel_provider_id = \
          remaining_providers.pop() if any(remaining_providers) else random.choice(all_provider_choices)
        new_group.save()


def create_locations(Location):
    faker = Faker()

    for _ in range(20):
        new_location = Location()
        new_location.name = faker.city()
        new_location.external_id = faker.random_int()
        new_location.secret_code = faker.uuid4()
        new_location.save()
