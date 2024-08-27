DC = docker compose
EXEC = docker exec -it
DB_CONTAINER = example-db
LOGS = docker logs
ENV = --env-file .env

APP_FILE = docker_compose/app.yml
CELERY_FILE = docker_compose/celery.yml
REDIS_FILE = docker_compose/redis.yml

APP_CONTAINER = app
REDIS_CONTAINER = redis
CELERY_BEAT_CONTAINER = celert_beat
CELERY_WORKER_CONTAINER = celery_worker

MANAGE_PY = python manage.py


.PHONY: app
app:
	${DC} -f ${APP_FILE} ${env} -f ${CELERY_FILE} ${ENV} -f${REDIS_FILE} up --build -d

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER}

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} down

.PHONY: migrate
migrate:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} migrate

.PHONY: migrations
migrations:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} makemigrations

.PHONY: superuser
superuser:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} createsuperuser

.PHONY: collectstatic
collectstatic:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} collectstatic

.PHONY: run-test
run-test:
	${EXEC} ${APP_CONTAINER} pytest


.PHONY: redis
redis:
	${DC} -f ${REDIS_FILE} up --build -d

.PHONY: redis-logs
redis-logs:
	${LOGS} ${REDIS_CONTAINER}


.PHONY: celery
celert:
	${DC} -f ${CELERY_FILE} up --build -d

.PHONY: celery-beat-logs
celery-beat-logs:
	${LOGS} ${CELERY_BEAT_CONTAINER}

.PHONY: celery-worker-logs
celery-worker-logs:
	${LOGS} ${CELERY_WORKER_CONTAINER}








run-local:
	python ./forum/manage.py runserver --settings=forum.settings
# worker:
# 	celery -A forum.celery worker -l info --pool=solo
# beat:
# 	celery -A forum.celery beat -l info
