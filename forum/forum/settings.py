"""
Django settings for forum project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path
from datetime import time

from dotenv import load_dotenv

load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get("DJANGO_SECRET")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG")


OWM_API_KEY = os.environ.get("OWN_API_KEY")


ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_celery_results",
    "django_celery_beat",
    "django_summernote",
    "rest_framework",
    "constance",
    "import_export",
    "django_admin_geomap",
    "api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "forum.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "forum.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB"),
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": os.environ.get("POSTGRES_HOST"),
            "PORT": os.environ.get("POSTGRES_PORT"),
        },
    }

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


SUMMERNOTE_CONFIG = {
    "iframe": True,
    "summernote": {
        "width": "100%",
        "height": "480",
        "lang": None,
        "toolbar": [
            ["style", ["style"]],
            ["font", ["bold", "underline", "clear"]],
            ["fontname", ["fontname"]],
            ["color", ["color"]],
            ["para", ["ul", "ol", "paragraph"]],
            ["table", ["table"]],
            ["insert", ["link", "picture", "video"]],
            ["view", ["fullscreen", "codeview", "help"]],
        ],
        "lang": "ko-KR",
    },
}

X_FRAME_OPTIONS = "SAMEORIGIN"

# from django.contrib.auth.models import User

CONSTANCE_CONFIG = {
    "REPICIENTS": (
        "ALL",
        "The list of repicient's email addresses who will receive the message",
        str,
    ),
    "THEME_OF_MESSAGE": ("News", "The theme of the message", str),
    "TEXT_OF_MESSAGE": ("Hello, world!", "The text of the message", str),
    "TIME_OF_SENDING_MESSAGE": (time(12, 30), "The time of sending message", time),
    "FROM_EMAIL": ("example@mail.ru", "The email address", str),
}
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"


# Celery Configuration Options
# CELERY_TIMEZONE = "Europe/Moscow"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_RESULT_BACKEND = "django-db"
CELERY_RESULT_EXTENDED = True

REDIS_PORT = os.environ.get("REDIS_PORT", 6379)

if DEBUG:
    CELERY_BROKER_URL = f"redis://localhost:{REDIS_PORT}/0"
else:
    CELERY_BROKER_URL = f"redis://redis:{REDIS_PORT}/0"

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# CELERY_USE_DEPRECATED_PYTZ = True

from import_export.formats.base_formats import XLSX

IMPORT_EXPORT_FORMATS = [XLSX]
