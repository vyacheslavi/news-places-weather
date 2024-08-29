import os

from celery import Celery
from celery.schedules import crontab

# from django_celery_beat.models import CrontabSchedule, PeriodicTask
from constance import config

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "forum.settings")
# os.environ["DJANGO_SETTINGS_MODULE"] = "forum.settings"

django.setup()

app = Celery("forum")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     schedule, _ = CrontabSchedule.objects.get_or_create(
#         minute=config.TIME_OF_SENDING_MESSAGE.minute,
#         hour=config.TIME_OF_SENDING_MESSAGE.hour,
#         day_of_week="*",
#         day_of_month="*",
#         month_of_year="*",
#     )
#     PeriodicTask.objects.create(
#         crontab=schedule,
#         name="Daily mailing of news",
#         task="api.tasks.send_emails_to_users",
#         kwargs={
#             "repicients": config.REPICIENTS,
#             "theme": config.THEME_OF_MESSAGE,
#             "text": config.TEXT_OF_MESSAGE,
#             "from_address": config.FROM_EMAIL,
#         },
#     )

app.conf.beat_schedule = {
    "news_mailing": {
        "task": "api.tasks.send_emails_to_users",
        "schedule": crontab(
            hour=config.TIME_OF_SENDING_MESSAGE.hour,
            minute=config.TIME_OF_SENDING_MESSAGE.minute,
        ),
        "kwargs": {
            "repicients": config.REPICIENTS,
            "theme": config.THEME_OF_MESSAGE,
            "text": config.TEXT_OF_MESSAGE,
            "from_address": config.FROM_EMAIL,
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
