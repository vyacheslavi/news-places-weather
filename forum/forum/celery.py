import os

from celery import Celery
from celery.schedules import crontab

from .constance import get_constance_setting

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "forum.settings")

django.setup()

app = Celery("forum")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


app.conf.beat_schedule = {
    "news_mailing": {
        "task": "api.tasks.send_emails_to_users",
        "schedule": crontab(
            hour=get_constance_setting("TIME_OF_SENDING_MESSAGE").hour,
            minute=get_constance_setting("TIME_OF_SENDING_MESSAGE").minute,
        ),
        "kwargs": {
            "repicients": get_constance_setting("REPICIENTS"),
            "theme": get_constance_setting("THEME_OF_MESSAGE"),
            "text": get_constance_setting("TEXT_OF_MESSAGE"),
            "from_address": get_constance_setting("FROM_EMAIL"),
        },
    },
    "collecting_weather_reports": {
        "task": "api.tasks.get_weather_from_places_task",
        "schedule": 60 * 60,
    },
}


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
