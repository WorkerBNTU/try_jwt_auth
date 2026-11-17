from celery import Celery
import time

celery_app = Celery(
    "tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)


@celery_app.task
def send_welcome_email(email):
    time.sleep(10)
    print(f"Письмо отправили на {email}")
    return 1 / 0
