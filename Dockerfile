
FROM python:3.12-slim

WORKDIR /app


RUN apt-get update && apt-get install -y gcc libpq-dev


COPY . /app/


RUN pip install --upgrade pip
RUN pip install -r requirements.txt


RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate


CMD ["gunicorn", "your_project_name.wsgi:application", "--bind", "0.0.0.0:8000"]