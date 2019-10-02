import os

class JSONSeedLoader():
    """
    Pre-fills the database with usable models (read from JSON input file)

    Params:
        json_input_path : a filename from settings.py's FIXTURE_DIRS

    Optimal conditions:
        migration 0001_initial present
    """

    def __init__(self, json_input_path):
        self.json_input_path = json_input_path


    def execute(self, _apps_registry, _schema_editor):
        os.system(f"python3 manage.py loaddata {self.json_input_path}")
