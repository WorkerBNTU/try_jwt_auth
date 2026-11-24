import os
from celery import Celery
import time

BROKER_URL = os.getenv("CELERY_BROKER", "redis://localhost:6379/0")
celery_app = Celery(
    "tasks", broker=BROKER_URL, backend=BROKER_URL
)


@celery_app.task
def send_welcome_email(email):
    time.sleep(10)
    print(f"Письмо отправили на {email}")
    return 1 / 0
