from datetime import time
from django.core.mail import send_mass_mail
from django.contrib.auth.models import User

from celery import shared_task
from celery.utils.log import get_task_logger
from django_celery_beat.models import PeriodicTask

from constance import config

logger = get_task_logger(__name__)


@shared_task
def send_emails_to_users(
    repicients: list[str],
    theme: str,
    text: str,
    from_address: str,
):
    if repicients is "ALL":
        users = User.objects.all()
        repicients = []
        for user in users:
            repicients.append(user.email)

    data_tuple = (theme, text, from_address, repicients)
    sending_mail = send_mass_mail(
        data_tuple,
        fail_silently=False,
    )
    print("Email Sent to " + str(len(repicients)) + " users")
    return sending_mail
