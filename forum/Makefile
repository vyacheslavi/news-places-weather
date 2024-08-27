run-local:
	python manage.py runserver --settings=forum.settings.local

worker:
    python -m celery -A forum worker --loglevel info

beat:
    python -m celery -A forum beat --loglevel info
