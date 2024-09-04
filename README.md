# news-places-weather

Проект сделан в качестве тестового задания.

stack:
Django, DRF, Celery

## В проекте реализован следующий функционал:

1. CRUD Новостей (DRF)
2. Интеграция summernote редактора в админ панель (django-summernote)
3. Асинхронная задача по рассылке сегодняшних новостей (django-celery-beat)
4. Возможность изменения настроек в run-time у асинхронной задачи (django-constance)
5. Импорт-експорт записей из базы данных с фильтрацией (django-import-export)
6. Интеграция виджета карты в админ панель (django-admin-geomap)
7. Асинхронная задачи на получение сводки погоды из внешнего API (pyowm, django-celery-beat)

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [GNU Make](https://www.gnu.org/software/make/)

## Run project with docker-compose

set in env file `DJANGO_DEBUG=false`

### Implemented Commands

 * `make app` - up application and database/infrastructure
 * `make app-logs` - follow the logs in app container
 * `make app-down` - down application and all infrastructure
 * `make redis-logs` - follow the logs in redis container
 * `make c-b-logs` - follow the logs in celery-beat container
 * `make c-w-logs` - follow the logs in celery-worker container

### Most Used Django Specific Commands

 * `make migration`s - make migrations to models
 * `make migrate` - apply all made migrations
 * `make collectstatic` - collect static
 * `make superuser` - create admin user

## Run project local

1. clone the project

`git clone https://github.com/vyacheslavi/news-places-weather.git`

2. create and start a a virtual environment

`python -m venv venv`

`venv/Scripts/activate`

3. Install the project dependencies:

`pip install poetry`

`poetry config virtualenvs.create false`

`poetry install`

4. create .env file and set

`DJANGO_DEBUG=true`

5. then run

`cd forum` # execute all commands from this directory

`python manage.py makemigrations`

`python manage.py migrate`

6. create admin account

`python manage.py createsuperuser`

7. to start the development server

`python manage.py runserver`

8. run redis in docker container

`docker compose -f docker-compose/redis.yml up --build -d`

9. run celery and celery-beat

`celery -A forum.celery worker -l info --pool=solo`

`celery -A forum.celery beat -l info`

10. and open localhost:8000 on your browser to view the app.
