# news-places-weather

Проект сделан в качестве тестового задания.

stack:
Django, DRF, Celery

В проекте реализован следующий функционал:
1) CRUD Новостей (DRF)
2) Интеграция summernote редактора в админ панель (django-summernote)
3) Асинхронная задача по рассылке сегодняшних новостей (django-celery-beat)
4) Возможность изменения настроек в run-time у асинхронной задачи (django-constance)
5) Импорт-експорт записей из базы данных с фильтрацией (django-import-export)
6) Интеграция виджета карты в админ панель (django-admin-geomap)
7) Асинхронная задачи на получение сводки погоды из внешнего API (pyowm, django-celery-beat)


docker compose сделал, но не тестил, т.к. ресурсов на ноуте не хватает.
Поэтому проверен только локальный запуск. Ключ к openweathermap.org прилагается.

## A few steps for cloning and run project

1) clone the project

`git clone https://github.com/vyacheslavi/news-places-weather.git`

2) create and start a a virtual environment

`python -m venv venv`

`venv/Scripts/activate`

3) Install the project dependencies:

`pip install poetry`

`poetry config virtualenvs.create false`

`poetry install`

4) then run

`cd forum` # execute all commands from this directory

`python manage.py makemigrations`

`python manage.py migrate`

5) create admin account

`python manage.py createsuperuser`

6) to start the development server

`python manage.py runserver`

7) run redis in docker container

`docker compose -f ../docker-compose/redis.yml up --build -d`

8) run celery and celery-beat

`celery -A forum.celery worker -l info --pool=solo`
`celery -A forum.celery beat -l info`

9) and open localhost:8000 on your browser to view the app.
