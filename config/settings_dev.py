import os

from .settings import BASE_DIR, INSTALLED_APPS


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db", "db.sqlite3"),
    }
}

DEBUG = True

INSTALLED_APPS += ["faker"]

SECRET_KEY = "g&1o*j=9#c7c3a3u@*85nb5jahlo!is5*v6z!&+noiy#6urp5*"
