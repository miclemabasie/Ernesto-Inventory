from celery import Celery, shared_task
import pyautogui

# Create a Celery app instance
app = Celery("your_project_name")

import pywhatkit
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
    pywhatkit.sendwhatmsg(number, message, hour, minute)
    url = "https://assets.mspimages.in/wp-content/uploads/2021/11/Whatsapp-Send-Button.jpg"
    # Get the coordinates of all instances of the button on the screen
    button_image = pyautogui.screenshot(url)
    whatsapp_send_button_coordinates = pyautogui.locateAllOnScreen(button_image)

    if whatsapp_send_button_coordinates is not None:
        pyautogui.click(whatsapp_send_button_coordinates)
    else:
        print("WhatsApp send button not found!")
    return "Done sending mail!"
