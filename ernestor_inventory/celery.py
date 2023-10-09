# from __future__ import absolute_import

# import os

# from celery import Celery
# from django.conf import settings

# # Set the Celery broker URL to the Redis installation directory
# CELERY_BROKER_URL = "redis://localhost:6379/0"


# os.environ.setdefault(
#     "DJANGO_SETTINGS_MODULE", "ernestor_inventory.settings.development"
# )

# # Create a Celery app instance
# app = Celery("ernestor_inventory")
# app.conf.enable_utc = False
# app.conf.update(timezone="Africa/Douala")

# # Load the Celery configuration from the Django settings file
# app.config_from_object(settings, namespace="CELERY")

# # Discover and register all Celery tasks in the project
# app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print(f"Request: {self.request!r}")


import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "ernestor_inventory.settings.development"
)
# Tell Celery to retry connecting to the broker on startup
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
app = Celery("ernestor_inventory")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
