from .json_seed_loader import JSONSeedLoader

"""
Pre-fills the database with usable models (read from JSON input file).

Usage:

    Command line:
        python3 manage.py loaddata seeds
            the "seeds" file is already there for you,
            but you can use any filename present in settings.py's FIXTURE_DIRS

    Python code:
        from panel_provider_pricing.migrations.seeding import JSONSeedLoader

        JSONSeedLoader("your_json_file.json").execute()
"""
