from .base import *


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": env("DATABASE"),
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
