from .base import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "railway",
        "USER": "postgres",
        "PASSWORD": "C65gBC363AfFAB2CcBdd4dF2a4gbceEB",
        "HOST": "viaduct.proxy.rlwy.net",
        "PORT": "36189",
    }
}
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.origin.sqlite3",
#     }
# }
