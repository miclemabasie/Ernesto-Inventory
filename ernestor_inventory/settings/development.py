from .base import *


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
# "default": {
# "ENGINE": env("DATABASE"),
# "NAME": BASE_DIR / "db.sqlite3",
# }
# }

#
DATABASES = {
    "default": {
        "ENGINE": env("DATABASE"),
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}
#
