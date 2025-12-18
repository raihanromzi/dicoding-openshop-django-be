setup:
	pipenv install

migrate:
	pipenv run python manage.py migrate

run:
	pipenv run python manage.py runserver