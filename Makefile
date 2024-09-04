DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file ./forum/.env
MANAGE_PY = python ./forum/manage.py

APP_FILE = docker_compose\app.yml
REDIS_FILE = docker_compose\redis.yaml

DB_CONTAINER = db
APP_CONTAINER = main-app
REDIS_CONTAINER = redis
CELERY_BEAT_CONTAINER = celery-beat
CELERY_WORKER_CONTAINER = celery-worker


.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d


.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER}

.PHONY: db-logs
db-logs:
	${LOGS} ${DB_CONTAINER}

.PHONY: redis-logs
redis:
	${LOGS} ${REDIS_CONTAINER}

.PHONY: c-b-logs
c-b-logs:
	${LOGS} ${CELERY_BEAT_CONTAINER}

.PHONY: c-w-logs
c-w-logs:
	${LOGS} ${CELERY_WORKER_CONTAINER}


.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} down

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
