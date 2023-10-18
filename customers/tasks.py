from celery import Celery, shared_task
import keyboard

# Create a Celery app instance
app = Celery("your_project_name")

# import pywhatkit
from datetime import datetime


@shared_task(bind=True)
def test_func(self):
    # Operations
    for i in range(120):
        print(i)
    return "Done!"


# Define the Celery task
@shared_task(bind=True)
def send_whatsapp_mail_to_customer(self, number, message):
    print("Start sending mail")
    time = datetime.now()
    hour = time.hour
    minute = time.minute + 1
    print(len(number), number)
    # pywhatkit.sendwhatmsg(number, message, hour, minute)
    return "Done sending mail!"
