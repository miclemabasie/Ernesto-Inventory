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
# DATABASES = {
#     "default": {
#         "ENGINE": env("DATABASE"),
#         "NAME": env("DB_NAME"),
#         "USER": env("DB_USER"),
#         "PASSWORD": env("DB_PASSWORD"),
#         "HOST": env("DB_HOST"),
#         "PORT": env("DB_PORT"),
#     }
# }
#

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "railway",
        "USER": "postgres",
        "PASSWORD": "eqs7n7ucX5SHxFXiu1CX",
        "HOST": "containers-us-west-102.railway.app",
        "PORT": "7463",
    }
}
