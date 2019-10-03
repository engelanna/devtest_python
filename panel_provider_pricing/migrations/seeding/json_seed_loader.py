import os

class JSONSeedLoader():
    """
    Pre-fills the database with usable models (read from JSON input file)

    Usage:

        Command line:
            python3 manage.py loaddata seeds
                the "seeds" file is already there for you,
                but you can use any filename present in settings.py's FIXTURE_DIRS

        Python code:
            Params:
                json_input_path : a filename from settings.py's FIXTURE_DIRS
            Example:
                from panel_provider_pricing.migrations.seeding import JSONSeedLoader

                JSONSeedLoader("your_json_file.json").execute()

        Optimal conditions:
            migration 0001_initial present
    """

    def __init__(self, json_input_path):
        self.json_input_path = json_input_path


    def execute(self):
        os.system(f"python3 manage.py loaddata {self.json_input_path}")
