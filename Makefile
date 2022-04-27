venv = poetry run
path = manage.py

server:
	$(venv) python $(path) runserver 0.0.0.0:9001

migrate:
	$(venv) python $(path) makemigrations
	$(venv) python $(path) migrate

rollback:
	$(venv) python $(path) migrate $(model) $(step)
