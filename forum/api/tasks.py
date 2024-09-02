from datetime import datetime
from django.core.mail import send_mass_mail
from django.contrib.auth.models import User

from celery import shared_task
from celery.utils.log import get_task_logger

from .models import News
from .services import get_weather_from_places

logger = get_task_logger(__name__)


@shared_task
def send_news_to_users(
    repicients: list[str] | str,
    theme: str,
    text: str,
    from_address: str,
):
    if repicients is "ALL":
        users = User.objects.all()
        repicients = []
        for user in users:
            repicients.append(user.email)

    urls = get_todays_news_url()
    text += urls

    data_tuple = (theme, text, from_address, repicients)
    sending_mail = send_mass_mail(
        data_tuple,
        fail_silently=False,
    )
    print("Email Sent to " + str(len(repicients)) + " users")
    return sending_mail


def get_todays_news_url() -> str | None:
    today = datetime.date.today()
    todays_news = News.objects.filter(created_at__date=today)
    if todays_news:
        urls = ""
        for news in todays_news:
            urls = (f"http://localhost:8000/api/v1/news/{news.id}/",)

        return urls


@shared_task
def get_weather_from_places_task():
    get_weather_from_places()
